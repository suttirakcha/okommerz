from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignInForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)    

class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input input-bordered w-full mt-2'}),
        label='Username',
        label_suffix=''
    )
    first_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'input input-bordered w-full mt-2'}),
        label='First name',
        label_suffix=''
    )
    last_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Surname', 'class': 'input input-bordered w-full mt-2'}),
        label='Surname',
        label_suffix=''
    )
    email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'input input-bordered w-full mt-2'}),
        label='Email',
        label_suffix=''
    )
    password1 = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input input-bordered w-full mt-2'}),
        label='Password',
        label_suffix=''
    )
    password2 = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'input input-bordered w-full mt-2'}),
        label='Confirm password',
        label_suffix=''
    )

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('address_title', 'address', 'city_or_county', 'state_or_province', 'country', 'postal_code')

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

class AccountDetailsForm(forms.Form):
    first_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'input input-bordered w-full mt-2'}),
        label='First name',
        label_suffix=''
    )
    last_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Surname', 'class': 'input input-bordered w-full mt-2'}),
        label='Surname',
        label_suffix=''
    )
    email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'input input-bordered w-full mt-2'}),
        label='Email',
        label_suffix=''
    )