from django.shortcuts import render
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, user_logged_out
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from . import forms

# Create your views here.

def shop(request):
    num_of_products = 6
    carousels = MarketingCampaign.objects.all()
    categories = ProductCategory.objects.all()
    products = ProductItem.objects.all()

    return render(request, 'shop.html', {'carousels': carousels, 'products': products, 'categories': categories, 'num_of_products': num_of_products})

def single_product(request, pk):
    product = get_object_or_404(ProductItem, pk=pk)
    user = request.user
    form = forms.AddToCartForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        quantity = form.cleaned_data['quantity']
        cart_item, created = CartItem.objects.get_or_create(
            user=user,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

    return render(request, 'single-product.html', {'form': form, 'product':product})

def login_acc(request):
    message = ''
    if request.method == 'POST':
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(redirect_to='/')
            else:
                message = 'Your username or password is incorrect. Please try again.'
    else:
        form = forms.SignInForm()

    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to='/')
    else:
        return render(request, 'login.html', context={'form': form, 'message': message})

def signup_acc(request):
    error_message = ''
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            confirm_password = form.cleaned_data['password2']

            if password == confirm_password:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )

                user = authenticate(request, username=username, password=password)
                login(request, user)

                return HttpResponseRedirect(redirect_to='/login')
            else:
                form.add_error('confirm_password', 'Passwords do not match')
                error_message = 'Passwords do not match'
        else: 
            error_message = 'There was an error while signing up. Please try again.'
    else:
        form = forms.SignUpForm()

    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to='/')
    else:
        return render(request, 'signup.html', {'form': form, 'message': error_message})

def logout_acc(request):
    logout(request)
    if user_logged_out:
        return HttpResponseRedirect(redirect_to='/')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def my_account(request):
    return render(request, 'my-account.html')

def add_to_cart(request, product_id):
    product = get_object_or_404(ProductItem, id=product_id)
    user = request.user
    form = forms.AddToCartForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        quantity = form.cleaned_data['quantity']
        cart_item, created = CartItem.objects.get_or_create(
            user=user,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return HttpResponseRedirect(redirect_to='cart/')
        
    return render(request, 'api/add_to_cart.html', {'form': form, 'product': product})

def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def search(request):
    search_result = ProductItem.objects.filter()
    return render(request, 'searchbar.html', {'results': search_result})

def checkout(request):
    return render(request, 'checkout.html')