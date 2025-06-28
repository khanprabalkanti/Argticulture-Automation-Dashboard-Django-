from rest_framework import serializers
from .models import sensorData, ActuatorState

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = sensorData
        fields = '__all__'

class ActuatorStateSerializer(serializers.ModelSerializer):  
    class Meta:
        model = ActuatorState
        fields = '__all__'