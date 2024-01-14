from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *

# Create your views here.

def shop(request):
    carousels = MarketingCampaign.objects.all()
    category = ProductCategory.objects.all()
    products = ProductItem.objects.all()
    return render(request, 'shop.html', {'carousels': carousels, 'products': products, 'categories': category})

def single_product(request, pk):
    products = get_object_or_404(ProductItem, pk=pk)
    return render(request, 'single-product.html', {'products':products})