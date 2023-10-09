from django.db import models

# Create your models here.
from django.db import models

class Users(models.Model):
    username = models.CharField(unique=True, max_length=255)
    total_points = models.IntegerField()
    objects = models.Manager()

class Payer(models.Model):
    payer_name = models.CharField(max_length=255)
    points_given = models.IntegerField(default=0)
    paid_to = models.ForeignKey(Users, on_delete=models.CASCADE)
    paid_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
