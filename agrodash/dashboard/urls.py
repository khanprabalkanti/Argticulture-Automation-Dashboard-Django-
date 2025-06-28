from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('api/sensor-data/', views.receive_sensor_data, name='sensor-data'),
    path('api/actuators/', views.get_actuator_state, name='get-actuators'),
    path('api/update-actuator/', views.update_actuator_state, name='update-actuator'),
]
