from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    email = models.EmailField()
    is_buyer = models.BooleanField(default=False)


class BuyerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null = True,related_name = 'buyer_profile')
    bio = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)

class ManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,null=True,related_name = 'manager_profile')
    nursery_name = models.CharField(max_length=100,blank=True)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	print('****', created)
	if instance.is_buyer:
		print('buyer')
		BuyerProfile.objects.get_or_create(user = instance)
	else:
		print('manager')
		ManagerProfile.objects.get_or_create(user = instance)
	
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	print('_-----')	
	# print(instance.internprofile.bio, instance.internprofile.location)
	if instance.is_buyer:
		print('buyerprofile')
		instance.buyer_profile.save()
	elif instance.is_buyer==False:
		print('manager.profile')
		#ManagerProfile.objects.get_or_create(user = instance)
		instance.manager_profile.save()
	else:
		print('get or create')
		ManagerProfile.objects.get_or_create(user = instance)


# @receiver(post_save, sender=User, dispatch_uid='save_new_manager')
# def save_profile(sender, instance, created, **kwargs):
# 	user = instance
# 	if created:
# 		user.manager_profile.save()
# 	else:
# 		ManagerProfile.objects.get_or_create(user = instance)