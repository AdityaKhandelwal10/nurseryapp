from django.shortcuts import render, redirect
from .forms import BuyerForm,ManagerForm,NewUserForm as UserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import ManagerProfile,BuyerProfile

def logout_request(request): #process logout request
    logout(request)
    messages.info(request,"You have successfully logged out ")
    print('logout is running')
    return redirect("/")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid() :
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= username,password =password)
            if user is not None :
                login(request, user)
                messages.info(request,f"You are now logged in as : {username}")
                print('login is running')
            else:
                 messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")


    form = AuthenticationForm
    return render(request = request,
     template_name = "core/login.html",
     context = {"form" : form})


def buyer_profile_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix = 'UF')
        profile_form = BuyerForm(request.POST,prefix ='PF')

        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save(commit=False)
            

            user.save()

            user.buyer_profile.bio = profile_form.cleaned_data.get('bio')
            user.buyer_profile.location = profile_form.cleaned_data.get('location')
            user.buyer_profile.save()

    else:
        user_form = UserForm(prefix='UF')
        profile_form = BuyerForm(prefix='PF')


    context ={
            'user_form': user_form,
            'profile_form': profile_form,
        }
    return render(request= request, template_name='core/buyer_profile.html',context =context)

def manager_profile_view(request):
    
    #request.user.is_buyer = False
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix = 'UF')
        profile_form1 = ManagerForm(request.POST,prefix ='PF')
        
        if user_form.is_valid() and profile_form1.is_valid():
            user = user_form.save(commit=False)
           
            
            user.save()
            print('Two')
            #print(request.user.is_buyer)
            user.manager_profile.nursery_name = profile_form1.cleaned_data.get('nursery_name')
            #user.manager_profile.location = profile_form.cleaned_data.get('location')
            user.manager_profile.save()

    else:
        user_form = UserForm(prefix='UF')
        profile_form1 = ManagerForm(prefix='PF')


    context ={
            'user_form': user_form,
            'profile_form': profile_form1,
        }
    return render(request= request, template_name='core/manager_profile.html',context =context)