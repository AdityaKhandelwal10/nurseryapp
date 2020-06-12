from django.db import models
from core.models import BuyerProfile
from nursery.models import Plants as Plants

class Cart(models.Model):
    
    buyer = models.OneToOneField(BuyerProfile,on_delete=models.CASCADE)
    plants = models.ManyToManyField(Plants)
    total_price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.buyer.user.username

class OrderPlaced(models.Model):
    buyer_op = models.ForeignKey(BuyerProfile,on_delete=models.CASCADE)
    plants_op = models.ManyToManyField(Plants)
    total_price_op = models.IntegerField(default=0)
    #order_id = models.AutoField(primary_key =True,null = False , unique = True)
    
    def __str__(self):
        return self.buyer_op.user.username
    