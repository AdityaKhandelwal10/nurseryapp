from django.urls import path,include
from . import views
urlpatterns = [
    
    path('manager-home/', views.home,name = 'manager_home'),
    path('add-plant/', views.add_plant,name = 'add_plant'),
    path('orders-received/', views.get_placed_orders, name= 'orders-received'),
]
