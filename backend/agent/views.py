
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from vendor.models import *
from rest_framework.response import Response
from .models import * 


class ListCheckinItemsForQA(views.APIView):
    permission_classes= (IsAuthenticated),
    
    def get(self, request, qa_id):
        print(qa_id,"qa_id")
        
        return Response({})