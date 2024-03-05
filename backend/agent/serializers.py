from rest_framework import serializers 
from .models import *    
class QaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QAGuy 
        fields = "__all__"
        
class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = QACheckIn 
        fields = "__all__"