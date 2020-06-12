from django.contrib import admin

from .models import OrderPlaced,Cart

admin.site.register(Cart)

admin.site.register(OrderPlaced)
