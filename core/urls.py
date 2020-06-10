from django.urls import path,include
from . import views
urlpatterns = [
    
    path('buyer/', views.buyer_profile_view,name = 'buyer_form'),
    path('manager/', views.manager_profile_view,name = 'manager_form'),
    path('logout/',views.logout_request, name = "logout"),
    path('login/',views.login_request, name = "login"),
]
