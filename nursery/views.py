from django.shortcuts import render, redirect
from .models import Plants
from .forms import AddPlantsForm
from core.forms import ManagerProfile
from django.contrib import messages
from buyer.models import OrderPlaced as OrderPlaced


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
    #end debug here

    form = AddPlantsForm
    if request.method == 'POST':
        plants = Plants.objects.create(manager = manager)
        print(plants)

        form = AddPlantsForm(request.POST, instance= plants)
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



def get_placed_orders(request):
    user = request.user
    manager = ManagerProfile.objects.get(user = user)

    print('Manager is retrieved')
    print(user)

    #get all cart objects
    # final_orders = OrderPlaced.

    # for ordered_plants in final_orders.filter(manager = manager):
    #     print("running inside the for loop")
    #     print(ordered_plants)

    return redirect('/')






