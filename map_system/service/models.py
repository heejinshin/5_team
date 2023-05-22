from django.db import models

class MyModel(models.Model):
    상호명 = models.CharField(max_length=100)
    업종코드 = models.CharField(max_length=10)
    업종분류명 = models.CharField(max_length=100)
    법정동명 = models.CharField(max_length=100)
    도로명 = models.CharField(max_length=100)
    경도 = models.FloatField()
    위도 = models.FloatField()
