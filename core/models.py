from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField()
    category = models.CharField(max_length=200,null = True)

    def __str__(self):
        return self.username


class BuyerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null = True,related_name = 'buyer_profile')
    bio = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user
    



class ManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,null=True,related_name = 'manager_profile')
    nursery_name = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user
    

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
	#print('****', created)
	if instance.category == 'Buyer':
		print('buyer')
		BuyerProfile.objects.get_or_create(user = instance)
	elif instance.category =='Manager':
		print('manager')
		ManagerProfile.objects.get_or_create(user = instance)
	else : pass
	
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	print('_-----')	
	# print(instance.internprofile.bio, instance.internprofile.location)
	if instance.category == 'Buyer':
		print('buyerprofile')
		instance.buyer_profile.save()
	elif instance.category =='Manager':
		print('manager.profile')
		#ManagerProfile.objects.get_or_create(user = instance)
		instance.manager_profile.save()
	else:
		pass


# @receiver(post_save, sender=User, dispatch_uid='save_new_manager')
# def save_profile(sender, instance, created, **kwargs):
# 	user = instance
# 	if created:
# 		user.manager_profile.save()
# 	else:
# 		ManagerProfile.objects.get_or_create(user = instance)

# @receiver(pre_save, sender=User)
# def change_if_buyer(sender, instance, *args, **kwargs):
	
# 	if instance.is_buyer:
# 		print('buyer')
# 		BuyerProfile.objects.get_or_create(user = instance)
# 	else:
# 		print('manager')
# 		ManagerProfile.objects.get_or_create(user = instance)