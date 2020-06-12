from django.urls import path,include
from . import views
urlpatterns = [
    
    path('buyer-home/', views.buyer_home,name = 'buyer_home'),
    path('buyer-cart/', views.orders_placed,name = 'buyer-cart'),
    path('add-to-cart/<int:pk>', views.add_to_cart,name = 'add-to-cart'),
    path('delete-item/<int:pk>', views.delete_item,name = 'delete-item'),
    path('placed-orders/',views.buy_cart, name= "placed-orders"),
    
]
