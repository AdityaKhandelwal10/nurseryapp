from django.db import models
from core.models import BuyerProfile
from nursery.models import Plants as Plants

class Cart(models.Model):
    
    buyer = models.OneToOneField(BuyerProfile,on_delete=models.CASCADE)
    plants = models.ManyToManyField(Plants)
    
    