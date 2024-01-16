from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    reenter_password = forms.CharField(max_length=255, widget=forms.PasswordInput)

