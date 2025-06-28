from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import sensorData, ActuatorState
from .serializers import SensorDataSerializer, ActuatorStateSerializer
from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'dashboard.html')


@api_view(['POST'])
def receive_sensor_data(request):
    serializer = SensorDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status":"success"})
    return Response(serializer.error, status = 400)

@api_view(['GET'])
def get_actuator_state(request):
    devices = ActuatorState.objects.all()
    serializer = ActuatorStateSerializer(devices, many  = True)
    return Response(serializer.data)

@api_view(['POST'])
def update_actuator_state(request):
    motor = request.data.get("motor")
    state = request.data.get("is_on")
    obj, created = ActuatorState.objects.get_or_create(motor = motor)
    obj.is_on = state
    obj._state()
    return Response({"status":"updated"})