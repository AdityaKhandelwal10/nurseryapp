from django.shortcuts import render
from .models import Plants
from .forms import AddPlantsForm
from core.forms import ManagerProfile


def home(request):
    print(request.user.username)
    return render(request, 'nursery/manager_home.html')

def add_plant(request):
    user =request.user
    manager = ManagerProfile.objects.get(user= user)

    plants = Plants.objects.filter(manager = manager)
    print(plants)


    form = AddPlantsForm
    context = {'form' : form}
    return render(request = request,template_name='nursery/add_plant.html', context = context)
