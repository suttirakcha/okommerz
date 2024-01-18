from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shop),
    path('product/<int:pk>', views.single_product),
    path('login/', views.login_acc),
    path('signup/', views.signup_acc),
    path('logout/', views.logout_acc),
    path('privacy-policy/', views.privacy_policy)
]