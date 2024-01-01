from django.db import models
from django.contrib.auth.models import User


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    amount = models.CharField(max_length=200)
    percent = models.CharField(max_length=200)
    months = models.CharField(max_length=200)
    percent_to_pay = models.CharField(max_length=200)
    monthly_payment = models.CharField(max_length=200)
    life_insurance = models.CharField(max_length=200)
    payments_insurance = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class PaymentHistory(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    paid_amount = models.CharField(max_length=100)
    initial_paid = models.CharField(max_length=100)
    percent_paid = models.CharField(max_length=100)
    life_insurance  = models.CharField(max_length=100)
    payments_insurance = models.CharField(max_length=100)
    paid_date = models.DateField()

   # def __str__(self):
    #   return f"{self.loan} - {self.paid_amount} - {self.initial_paid} - {self.percent_paid} - {self.paid_date}"

