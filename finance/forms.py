from datetime import datetime, timedelta
from django import forms
from .models import Loan


class AddLoan(forms.Form):
    time_now = datetime.now() + timedelta(hours=4)
    name = forms.CharField(label="დასახელება", max_length=400, widget=forms.TextInput(attrs={"class": "form-control"}))
    amount = forms.CharField(label="საწყისი თანხა", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    percent = forms.CharField(label="საპროცენტო განაკვეთი", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    months = forms.CharField(label="ვადა (თვე)", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    percent_to_pay = forms.CharField(label="პროცენტი (სრული)", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    monthly_payment = forms.CharField(label="ყოველთვიური გადასახადი", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    life_insurance = forms.CharField(label="სიცოცხლის დაზღვევა", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    payments_insurance = forms.CharField(label="საკრედიტო შენატანების დაზღვევა", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))


class AddPayment(forms.Form):
    time_now = datetime.now() + timedelta(hours=4)
    name = forms.ModelChoiceField(label="დასახელება", queryset=Loan.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    amount = forms.CharField(label="გადახდილი თანხა", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    initial = forms.CharField(label="ძირი თანხა", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    payment_date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))