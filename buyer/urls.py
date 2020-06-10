from django.urls import path,include
from . import views
urlpatterns = [
    
    path('buyer-home/', views.buyer_home,name = 'buyer_home'),
    
    
]
