from django.db import models

class sensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    water_level = models.FloatField()

class ActuatorState(models.Model):
    motor = models.BooleanField()
    is_on = models.FloatField()

