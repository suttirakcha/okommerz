from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, user_logged_out
from .models import *
from . import forms

# Create your views here.

def shop(request):
    carousels = MarketingCampaign.objects.all()
    category = ProductCategory.objects.all()
    products = ProductItem.objects.all()
    return render(request, 'shop.html', {'carousels': carousels, 'products': products, 'categories': category})

def single_product(request, pk):
    products = get_object_or_404(ProductItem, pk=pk)
    return render(request, 'single-product.html', {'products':products})

def login_acc(request):
    form = forms.SignInForm()
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

    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to='/')
    else:
        return render(request, 'login.html', context={'form': form, 'message': message})

def logout_acc(request):
    logout(request)
    if user_logged_out:
        return HttpResponseRedirect(redirect_to='/')