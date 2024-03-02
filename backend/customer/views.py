from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from vendor.models import *
from rest_framework.response import Response
from vendor.serializers import (
    VendorSerializer,
    VehicleSerializer,
    CreateOrderSerializer,
)
from rest_framework import status
from django.db.models import Max
from datetime import datetime
import json


class ListVendors(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        if serializer.data:
            return Response({"data": serializer.data})
        else:
            return Response(
                {"data": "no vendor data found"}, status=status.HTTP_404_NOT_FOUND
            )


class ListVehiclesByVendor(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, vendor_id):
        vehicles = Vehicle.objects.filter(vendor_id=vendor_id)
        serializer = VehicleSerializer(vehicles, many=True)
        vendor = Vendor.objects.get(id=vendor_id)
        for vehicle in serializer.data:
            vehicle["vendor_name"] = vendor.name
            vehicle["vendor_details"] = vendor.details
        if serializer.data:
            return Response(serializer.data)
        else:
            return Response(
                {"msg": "no vehicles found for vendor"},
                status=status.HTTP_404_NOT_FOUND,
            )


class CreateOrder(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        print(json.dumps(data, indent=4))

        order_id = Order.objects.aggregate(Max("id"))["id__max"] or 0
        order_id = order_id + 1

        data["id"] = order_id

        date_of_booking = data["date_of_booking"]
        delivery_date = data["delivery_date"]

        purchase_order_number = f"{order_id}_{date_of_booking}"
        delivery_challan_number = f"{order_id}_{delivery_date}"

        data["purchase_order_number"] = purchase_order_number
        data["delivery_challan_number"] = delivery_challan_number

        print("data going to serializer")
        print(data)
        # Create the order
        serializer = CreateOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
