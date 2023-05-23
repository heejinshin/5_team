from django.db import models

class MyModel(models.Model):
    store_name = models.CharField(max_length=100)
    store_code = models.CharField(max_length=10)
    store_segment = models.CharField(max_length=100)
    address_dong = models.CharField(max_length=100)
    address_road = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
