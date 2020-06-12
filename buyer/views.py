from django.shortcuts import render,redirect
from nursery.models import Plants
from core.models import BuyerProfile
from .models import Cart, OrderPlaced

def buyer_home(request):
    
    plants = Plants.objects.all()
    context= {'plants' : plants}
    return render(request= request, template_name ='buyer/buyer_home.html', context = context)

#view to see what orders have been placed by the user
def orders_placed(request):
    user = request.user
    print(user) 
    buyer = BuyerProfile.objects.get(user= user)
    cart_id = Cart.objects.get(buyer=buyer)
    print(cart_id.pk)

    #orders = Cart.objects.get(id = cart_id.pk)
    orders = cart_id
    context={'orders' : orders}
    return render(request=request, template_name = 'buyer/cart.html', context = context)

#view to add item to the cart
# def add_to_cart(request,pk): #primary key in of plants
#     user = request.user
    
#     buyer = BuyerProfile.objects.get(user__username= user)
#     print(buyer)
#     print('before if')
    
#     if not buyer in Cart.objects.all():
#         cart = Cart()
#         cart.buyer.add(buyer)
        
    
#     #cart = Cart.objects.get(buyer = buyer) 
#     plant = Plants.objects.get(pk=pk)
#     if not plant in cart.plants.all():
#         cart.plants.add()
#     else:
#         print('Already there')

#     return redirect('buyer-cart/')

def add_to_cart(request,pk):
    user = request.user
    buyer = BuyerProfile.objects.get(user = user)
    print(user)
    print('\n1 is working\n')
    

    print('\n2nd block is starting\n')
    try:
        cart, created = Cart.objects.get_or_create(buyer = buyer)
    except :
        pass

    print('2nd block ends here \n')
    print(cart)

    print('\n 3rd block starting here\n')
    plant = Plants.objects.get(id = pk)
    print(plant)

    cart.plants.add(plant)
    print('\n 3rd block ends here\n')
    print('Added the item')

    return redirect('/buyer/buyer-cart/')

def delete_item(request,pk):
    user = request.user
    buyer = BuyerProfile.objects.get(user = user)
    print(user)
    print('\n1 is working\n')
    print('2nd block ends here \n')
    cart = Cart.objects.get(buyer = buyer)
    print(cart)

    print('\n 3rd block starting here\n')
    plant = Plants.objects.get(id = pk)
    print(plant)

    cart.plants.remove(plant)
    print('\n 3rd block ends here\n')
    

    return redirect('/buyer/buyer-cart/')


#configure total price as well

def buy_cart(request):
    user = request.user
    buyer = BuyerProfile.objects.get(user = user)
    print(user)
    print('\n1 is working\n')
    print('2nd block ends here \n')
    cart = Cart.objects.get(buyer = buyer)
    print(cart)

    print('\n 3rd block starting here\n')
    # plant = Plants.objects.get(id = pk)
    # print(plant)

    #cart.plants.remove(plant)
    print('\n 3rd block ends here\n')
    
    print('\n Fourth block starts here')
    
    placed_orders = OrderPlaced.objects.create(buyer_op = buyer)
    print(placed_orders.pk)

    if cart.plants.all is not None:

        for plant in cart.plants.all():
            print(plant)
            placed_orders.plants_op.add(plant)
    
        context = {'orders' : placed_orders}
        return render(request = request, template_name = 'buyer/placed_orders.html', context = context)

        
    else:
        
        return render(request = request, template_name = 'buyer/placed_orders.html', context ={})


