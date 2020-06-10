from django.contrib import admin
from .models import User,BuyerProfile,ManagerProfile


admin.site.register(User)
admin.site.register(BuyerProfile)
admin.site.register(ManagerProfile)

# Register your models here.
