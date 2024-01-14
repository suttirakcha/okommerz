from django.contrib import admin
from .models import *

# Register your models here.

class ProductLists(admin.ModelAdmin):
    list_display = ['product_name', 'regular_price', 'sales_price', 'product_category', 'created_at', 'updated_at']

class AddressLists(admin.ModelAdmin):
    list_display = ['address_title', 'city_or_county', 'state_or_province', 'country']

class ProductCategoryLists(admin.ModelAdmin):
    list_display = ['category']

class MarketingCampaignLists(admin.ModelAdmin):
    list_display = ['campaign_name', 'campaign_description']

admin.site.register(ProductItem, ProductLists)
admin.site.register(Address, AddressLists)
admin.site.register(ProductCategory, ProductCategoryLists)
admin.site.register(MarketingCampaign, MarketingCampaignLists)