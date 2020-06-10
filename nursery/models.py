from django.db import models
from core.models import User,ManagerProfile as ManagerProfile, BuyerProfile as BuyerProfile

# Need a plants model which will hold all the models and help in doing other things 

class Plants(models.Model):
    manager = models.ForeignKey(ManagerProfile,on_delete=models.CASCADE)
    plant_name = models.CharField(max_length=200)
    plant_desc = models.CharField(max_length=200)
    plant_price = models.IntegerField()

