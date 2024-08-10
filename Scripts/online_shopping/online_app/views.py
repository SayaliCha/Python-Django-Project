from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect,get_object_or_404

from django.contrib.auth.decorators import login_required
from.models import *
from django.contrib.auth.models import User
from .models import Product,Cart,CartItem
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

def home_view(request):
    pl=Product.objects.all()
    context={'pl':pl}
    return render(request,'home.html',context)
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a success page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a success page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
        logout(request)
        return redirect('/')  # Redirect to a success page


#def category_product_list(request):
 #   categories = Category.objects.all()
  #  context = {
  #      'categories': categories,
   # }
    #return render(request, 'category_product_list.html', context)


def sidebar(request):
    fname=request.session.get('fname',None)
    cate=Category.objects.all()
    context={'Cate':cate,'fname':fname}
    return render(request,'category_list.html',context)

def category_view(request):
    fname=request.session.get('fname',None)
    cate=Category.objects.all()
    card=Product.objects.all()
    context={'fname':fname,'Cate':cate,'Card':card}
    return render(request,'category.html',context)

def category_page(request,category_name):
    fname=request.session.get('fname',None)
    cate=Category.objects.all()
    card=Product.objects.all()
    filtered_product=Product.objects.filter(category_name=category_name)
    context={'fname':fname,'Cate':cate,'f_product':filtered_product,'Card':card}
    return render(request,'category.html',context)

def filter_cate(request,pid):
    # cateid=Category.objects.get(id=pid)
    fname=request.session.get('fname',None)
    product=Product.objects.filter(category_id=pid)
    cate=Category.objects.all()
    card=Product.objects.all()
    context={'Cate':cate,'product':product,'fname':fname,'Card':card}
    return render(request,'cat.html',context)





@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')

@login_required
def increase_item_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

@login_required
def decrease_item_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def view_cart(request):
   cart = Cart.objects.get(user=request.user)
   items = cart.items.all()
#    total_amount = sum(item.product.price * item.quantity for item in items)
#    context={'items': items, 'total_amount': total_amount}
#    context['razorpay_key_id']= settings.RAZORPAY_KEY_ID
   total_amount = sum((item.product.price) * item.quantity for item in items)
   final_amount = total_amount * 100
    
   context = {'items': items, 'total_price': total_amount, 'final_price': final_amount}
   context['razorpay_key_id']= settings.RAZORPAY_KEY_ID
   return render(request, 'view_cart.html',context )





from .models import cloth
import razorpay
def order(request):
    if request.method=='POST':
        name=request.POST.get('name')
        amount=int(request.POST.get('amount')) * 100
        print(name,amount)
        currency = 'INR'
        razorpay_client=razorpay.Client(auth=('rzp_test_6K659PBJWqIij9','kv0VVovqNqD37zzLhjiVVFXM'))
        payment = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='1'))
        print(payment)
        Cloth=cloth(name=name,amount=amount,payment_id = payment['id'])
        Cloth.save()
        return render(request,'order.html',{'payment': payment})
    else:
        return render(request,'order.html')
        
@csrf_exempt

def success1(request):
    if request.method=='POST':
        a=request.POST
        print(a)
        return render(request,'cart_success.html')
    else:
        return render(request,'cart_success.html')