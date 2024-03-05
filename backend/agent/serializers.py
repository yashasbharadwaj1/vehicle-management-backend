from .models import * 
from rest_framework import serializers

class QaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QAGuy 
        fields = "__all__"
