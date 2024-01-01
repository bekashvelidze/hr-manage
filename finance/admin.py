from django.contrib import admin
from .models import Loan, PaymentHistory

# Register your models here.

class LoanAdmin(admin.ModelAdmin):
    list_display=('name','amount','percent','life_insurance','payments_insurance','months','monthly_payment','user')

class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display=('loan','paid_amount','initial_paid','percent_paid','life_insurance','payments_insurance','paid_date')

admin.site.register(Loan, LoanAdmin)
admin.site.register(PaymentHistory, PaymentHistoryAdmin)
