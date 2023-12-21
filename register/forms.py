from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": 'form-control', 'required':'required'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control', 'required':'required'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control', 'required':'required'}))

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
        widgets = {
            'username':forms.TextInput(attrs={"class": 'form-control', 'required':'required'}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'required':'required'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'required':'required'}),
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User()
        fields = ["username", "email", "first_name", "last_name"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]