from django.contrib import admin
from .models import Loan, PaymentHistory

# Register your models here.

admin.site.register(Loan)
admin.site.register(PaymentHistory)
