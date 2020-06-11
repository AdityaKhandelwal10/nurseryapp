from django.shortcuts import render
from .models import Plants
from .forms import AddPlantsForm
from core.forms import ManagerProfile
from django.contrib import messages


def home(request):
    
    user =request.user
    print(user) 
    manager = ManagerProfile.objects.get(user__username= user)
    plants = Plants.objects.filter(manager = manager)

    context = {'plants' : plants,
            'manager' : manager}
    return render(request, 'nursery/manager_home.html',context)

def add_plant(request):
    #debugging
    user =request.user
    print(user)
    manager = ManagerProfile.objects.get(user__username= user)
    print(manager)

    plants = Plants.objects.filter(manager = manager)
    print(plants)
    #end debug here

    form = AddPlantsForm
    if request.method == 'POST':
        form = AddPlantsForm(request.POST)
        if form.is_valid():
            print("valid")
            plant = form.save()
            messages.success(request,f"New Plant added")

        else:
            return redirect('#')

    else:
        # for msg in form.error_messages:
        #     messages.error(request,f"{msg} : {form.error_messages[msg]}")
        pass


    #form = AddPlantsForm(initial={'manager' : manager})
    
    context = {'form' : form}
    return render(request = request,template_name='nursery/add_plant.html', context = context)





