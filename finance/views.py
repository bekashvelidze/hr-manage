from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Loan, PaymentHistory
from .forms import AddLoan, AddPayment
# from .filters import OrderFilter

@login_required(login_url='/login/')
def addloan(response):
    if response.method == "POST":
        form = AddLoan(response.POST)

        if form.is_valid():
            user_id = response.user.id
            name = form["name"].value()
            amount = form["amount"].value()
            percent = form["percent"].value()
            months = form["months"].value()
            percent_to_pay = form["percent_to_pay"].value()
            monthly_payment = form["monthly_payment"].value()
            life_insurance = form["life_insurance"].value()
            payments_insurance = form["payments_insurance"].value()
            date = datetime.now().now().date()
            time = datetime.now().now().time().strftime("%H:%M:%S")
            loan = Loan(name=name, amount=amount, percent=percent, months=months,
                            percent_to_pay=percent_to_pay, monthly_payment=monthly_payment,
                            life_insurance=life_insurance, payments_insurance=payments_insurance, date=date, time=time, user_id=user_id)
            loan.save()

            return HttpResponseRedirect("/")
    else:
        form = AddLoan()

    return render(response, "new_loan.html", {"form": form})


@login_required(login_url='/login/')
def pay(response):
    if response.method == "POST":
        loans = Loan.objects.filter(user=response.user)
        payform = AddPayment(response.POST)
        if payform.is_valid():
            amount_paid = payform["amount"].value()
            initial_paid = payform["initial"].value()
            date = datetime.now().now().date()
            loan_name = loans.get(id=int(payform["name"].value()))
            life_insurance = Loan.objects.filter(name__startswith=loan_name).values('life_insurance')[0]['life_insurance']
            payments_insurance = Loan.objects.filter(name__startswith=loan_name).values('payments_insurance')[0]['payments_insurance']
            percent_paid = round(float(amount_paid) - float(initial_paid) - float(life_insurance) - float(payments_insurance), 3)
            payment_history = PaymentHistory(loan=loan_name, paid_amount=amount_paid, initial_paid=initial_paid, percent_paid=percent_paid,
            life_insurance=life_insurance, payments_insurance=payments_insurance, paid_date=date)
            payment_history.save()

            return HttpResponseRedirect("/")
    else:
        payform = AddPayment()

    return render(response, "new_payment.html", {"payform": payform})


@login_required(login_url='/login/')
def myloans(response):
    user = response.user
    loans = Loan.objects.all().filter(user=user).order_by('-id')
    return render(response, "my_loans.html", {"loans": loans})


@login_required(login_url='/login/')
def loan(response, id):
    loan = Loan.objects.get(id=id)
    payment_history = PaymentHistory.objects.filter(loan=loan).order_by('-id')
    return render(response, "loan.html", {"loan": loan, "payment_history": payment_history})

