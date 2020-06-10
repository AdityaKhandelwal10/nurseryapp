from django.shortcuts import render
from nursery.models import Plants

def buyer_home(request):
    
    plants = Plants.objects.all()
    context= {'plants' : plants}
    return render(request= request, template_name ='buyer/buyer_home.html', context = context)
