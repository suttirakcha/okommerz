from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shop),
    path('product/<int:pk>', views.single_product),
    path('login/', views.login_acc),
    path('signup/', views.signup_acc),
    path('logout/', views.logout_acc),
    path('privacy-policy/', views.privacy_policy),
    path('my-account/', views.my_account),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
]