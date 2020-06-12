from django.shortcuts import render, redirect
from .models import Plants
from .forms import AddPlantsForm
from core.forms import ManagerProfile
from django.contrib import messages
from buyer.models import OrderPlaced as OrderPlaced
from django.contrib.auth.decorators import user_passes_test, login_required

#Make custom decorators here to check user permissions
def manager_check(user):
    if not user.is_superuser:
        entries = ManagerProfile.objects.all()
        print(user)
        return entries.filter(user=user).exists()
    else:
        return user.is_superuser


@login_required(login_url = '/login/')
@user_passes_test(manager_check, login_url = '/login/')
def home(request):
    
    user =request.user
    print(user)
    try:
        manager = ManagerProfile.objects.get(user__username= user)
        plants = Plants.objects.filter(manager = manager)

        context = {'plants' : plants,
                'manager' : manager}
    except:
        context={}
    return render(request, 'nursery/manager_home.html',context)


@login_required(login_url = '/login/')
@user_passes_test(manager_check, login_url = '/login/')
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



@login_required(login_url = '/login/')
@user_passes_test(manager_check, login_url = '/login/')
def get_placed_orders(request):
    user = request.user
    manager = ManagerProfile.objects.get(user = user)
    print(manager)
    print('Manager is retrieved')
    print(user)

    received_orders = OrderPlaced.objects.filter(plants_op__manager = manager)
    
    if received_orders is not None:
        context = {'orders' : received_orders}
        print(received_orders)
        
        return render(request =request , template_name = 'nursery/received_orders.html', context = context)


    else:
        context = {}
        return render(request =request , template_name = 'nursery/received_orders.html', context = context)









