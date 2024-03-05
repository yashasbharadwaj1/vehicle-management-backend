from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from vendor.models import *
from rest_framework.response import Response
from vendor.serializers import *
from rest_framework import status
from django.db.models import Max
from datetime import datetime
import json
from userauths.models import User
from django.db.models import Q
from django.db.models import F
from agent.models import *


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

        vehicles = Vehicle.objects.exclude(is_ordered=True).filter(vendor_id=vendor_id)
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
        product_id = data["product_id"]
        try:
            vehicle_obj = Vehicle.objects.get(id=product_id) 
            is_ordered = vehicle_obj.is_ordered 
            if is_ordered:
                return Response({"msg":"Vehicle already ordered"},status=status.HTTP_200_OK)
                
        except Vehicle.DoesNotExist:
            return Response({"msg":f"given vehicle id {product_id} does not exist"},status=status.HTTP_400_BAD_REQUEST)
        
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
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            order_data = serializer.data

            vehicle_id = order_data["product_id"]
            
            vehicle_obj = Vehicle.objects.get(id=vehicle_id)
            
            vehicle_obj.is_ordered = True
            vehicle_obj.save()

            return Response(order_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListOrders(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, customer_id):
        final_data = []

        orders_objs = Order.objects.filter(user_id=customer_id)
        orders_serializer = OrderSerializer(orders_objs, many=True)
        orders_data = orders_serializer.data

        if orders_data:
            for order_data in orders_data:
                data = {}
                vendor_id = order_data["vendor_id"]
                vehicle_id = order_data["product_id"]

                vendor_obj = Vendor.objects.get(id=vendor_id)
                vehicle_obj = Vehicle.objects.get(id=vehicle_id)

                vehicle_serializer = VehicleSerializer(vehicle_obj)
                vendor_serializer = VendorSerializer(vendor_obj)

                vehicle_data = vehicle_serializer.data
                vendor_data = vendor_serializer.data

                data["order_data"] = order_data
                data["vehicle_data"] = vehicle_data
                data["vendor_data"] = vendor_data

                final_data.append(data)

            return Response(final_data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"msg": f"No orders found for Customer with id {customer_id}"},
                status=status.HTTP_404_NOT_FOUND,
            )


class CheckinVehicle(views.APIView):
    permission_classes = ((IsAuthenticated),)

    def post(self, request):
        data = request.data

        print("data sent to checkin")
        print(json.dumps(data, indent=4))

        vehicle_number = data.get("vehicleNumber")
        vehicle_type = data.get("vehicleType")
        delivery_challan = data.get("deliveryChallan")
        purchase_order = data.get("purchaseOrder")

        try:
            order_obj = Order.objects.get(purchase_order_number=purchase_order)
            order_id = order_obj.id
            print(order_id, "order_id")
            user_id = order_obj.user_id_id
            print(user_id, "user_id")
            user_obj = User.objects.get(id=user_id)
            vehicle_id = order_obj.product_id_id
            print(vehicle_id, "vehicle id")
            vendor_id = order_obj.vendor_id_id
            print(vendor_id, "vendor id")

            vehicle_obj = Vehicle.objects.get(id=vehicle_id)
            if vehicle_obj.number != vehicle_number:
                return Response(
                    {"msg": "Please enter a valid vehicle number"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            if vehicle_obj.type != vehicle_type:
                return Response(
                    {"msg": "Please enter a valid vehicle type"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            if order_obj.delivery_challan_number != delivery_challan:
                return Response(
                    {"msg": "Please enter a valid delivery challan number."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            order_life_cycle_queryset = OrderLifeCycle.objects.filter(order_id=order_id)
            if order_life_cycle_queryset.exists():
                print(order_life_cycle_queryset)
                return Response(
                    {"msg": "Checkin already done"}, status=status.HTTP_200_OK
                )
            else:
                order_life_cycle_obj = OrderLifeCycle.objects.create(
                    order_id=order_obj, is_checkin_initiated=True, user_id=user_obj
                )
                order_life_cycle_obj.save()
                try:
                    newly_created_order_life_cycle_obj = OrderLifeCycle.objects.get(
                        order_id=order_obj, is_checkin_initiated=True, user_id=user_obj
                    )
                    order_life_cylce_id = newly_created_order_life_cycle_obj.id
                    qa_obj = QAGuy.objects.get(vendor=vendor_id)
                    qa_id = qa_obj.id
                    print(qa_id,"qa_id")
                    unique_checkin_id = f"{order_life_cylce_id}_{order_id}_{vehicle_id}_{user_id}_{qa_id}"
                    qa_check_in_obj = QACheckIn.objects.create(
                        qa_guy=qa_obj, unique_checkin_id=unique_checkin_id
                    )
                    qa_check_in_obj.save()
                except QAGuy.DoesNotExist:
                    return Response(
                        {
                            "msg": f"Vendor with id {vendor_id} has not yet assigned a qa guy hence checkout not initiated"
                        },
                        status=status.HTTP_200_OK,
                    )
                except OrderLifeCycle.DoesNotExist:
                    return Response(
                        {"msg": f"there is an issue with creating order life cycle"}
                    )

                return Response({"checkin initiated"}, status=status.HTTP_200_OK)

        except Order.DoesNotExist:
            return Response(
                {"msg": "Please enter a valid purchase order number. "},
                status=status.HTTP_404_NOT_FOUND,
            )

class CheckinStatus(views.APIView):
    permission_classes  =(IsAuthenticated),
    
    def get(self, request, customer_id):
        print(customer_id,"customer_id")
        try:
            user_obj = User.objects.get(id=customer_id) 
        except User.DoesNotExist:
            return Response({"msg":f"User with {customer_id} does not exist"},status=status.HTTP_400_BAD_REQUEST)
        
        order_life_cycle_queryset = OrderLifeCycle.objects.filter(user_id=user_obj)
        if order_life_cycle_queryset.exists():
            serializer = OrderLifeCycleSerializer(order_life_cycle_queryset,many=True) 
            order_life_cylce_data = serializer.data 
            for data in order_life_cylce_data:
                order_id = data["order_id"]
                order_obj = Order.objects.get(id=order_id)
                purchase_order_number = order_obj.purchase_order_number 
                data['purchase_order_number'] = purchase_order_number
                
            return Response(order_life_cylce_data,status=status.HTTP_200_OK)
        else:
            return Response({"msg":f"No checkins available for user"},status=status.HTTP_200_OK)
            
        