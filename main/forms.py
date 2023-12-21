from django import forms
from .models import Warehouse, Location, Type, Item


class CreateWarehouse(forms.Form):
    name = forms.CharField(label="სახელი", max_length=200)


class AddNewItem(forms.Form):
    item_number = forms.IntegerField(label="ნომერი", widget=forms.NumberInput(attrs={"class": "form-control"}))
    type = forms.ModelChoiceField(label="ინვენტარის ტიპი", queryset=Type.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    owner = forms.CharField(label="მფლობელი", max_length=250, widget=forms.TextInput(attrs={"class": "form-control"}))
    company = forms.ModelChoiceField(label="კომპანია", queryset=Warehouse.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    description = forms.CharField(label="აღწერა", widget=forms.Textarea(attrs={"rows": "5", "class":"form-control"}))
    photo_url = forms.ImageField(widget=forms.FileInput(attrs={"class": "fileinput"}))
    location = forms.ModelChoiceField(label="ლოკაცია", queryset=Location.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
