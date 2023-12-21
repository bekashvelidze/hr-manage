from datetime import datetime, timedelta
from django import forms
from .models import Category, Status


class CreateDepartment(forms.Form):
    name = forms.CharField(label="სახელი", max_length=200)


class AddNewTicket(forms.Form):
    time_now = datetime.now() + timedelta(hours=4)
    category = forms.ModelChoiceField(label="კატეგორია", queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    phone = forms.CharField(label="ტელეფონი", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(label="აღწერა", widget=forms.Textarea(attrs={"rows": "5", "class":"form-control"}))


class UpdateTicket(forms.Form):
    category = forms.ModelChoiceField(label="სტატუსი", queryset=Status.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))