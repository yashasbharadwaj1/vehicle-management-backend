from django.shortcuts import render
from rest_framework.views import views 
from rest_framework.permissions import  IsAuthenticated 
from vendor.models import *

class ListVehicles(views.APIView):
    permission_classes = (IsAuthenticated,) 
    
    def get(self, request):
        pass
    