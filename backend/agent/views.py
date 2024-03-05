from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated
from vendor.models import *
from rest_framework.response import Response
from .models import *
from .serializers import *
from vendor.serializers import *

class ListCheckinItemsForQA(views.APIView):
    permission_classes = ((IsAuthenticated),)

    def get(self, request, qa_id):
        print(qa_id, "qa_id")
        checkin_queryset = QACheckIn.objects.filter(qa_guy=qa_id)
        print(checkin_queryset)
        if checkin_queryset.exists():
            serializer = CheckinSerializer(checkin_queryset, many=True)
            checkin_data = serializer.data
            for data in checkin_data:
                unique_checkin_id = data.get("unique_checkin_id")
                #  unique_checkin_id = f"{order_life_cylce_id}_{order_id}_{vehicle_id}_{user_id}_{qa_id}"
                ids_list = unique_checkin_id.split("_")
                vehicle_id = ids_list[2]
                print(vehicle_id)

                vehicle_obj = Vehicle.objects.get(id=vehicle_id) 
                serializer = VehicleSerializer(vehicle_obj)
                vehicle_data = serializer.data 
                vehicle_name = vehicle_data['name'] 
                vehicle_number = vehicle_data['number'] 
                data["vehicle_name"] = vehicle_name 
                data["vehicle_number"] = vehicle_number 
                
            return Response(checkin_data,status=status.HTTP_200_OK)
        else:
            return Response(
                {"msg": "No checkins avilable for qa"}, status=status.HTTP_200_OK
            )
