from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, user_logged_out
from django.contrib.auth.models import User
from .models import *
from . import forms

# Create your views here.

def shop(request):
    carousels = MarketingCampaign.objects.all()
    categories = ProductCategory.objects.all()
    products = ProductItem.objects.filter()
    return render(request, 'shop.html', {'carousels': carousels, 'products': products, 'categories': categories})

def single_product(request, pk):
    products = get_object_or_404(ProductItem, pk=pk)
    return render(request, 'single-product.html', {'products':products})

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
            error_message = 'There was an error while signing in. Please try again.'
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