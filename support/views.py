from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Department, Ticket, Priority, Category, Status
from .forms import AddNewTicket
from .filters import OrderFilter


@login_required(login_url='/login/')
def support(response):
    if response.method == "POST":
        form = AddNewTicket(response.POST)
        departments = Department.objects
        priorities = Priority.objects
        categories = Category.objects

        if form.is_valid():
            category = categories.get(id=int(form["category"].value()))
            department = category.department
            priority = category.priority
            user = response.user.get_full_name()
            phone = form["phone"].value()
            date = datetime.now().now().date()
            time = datetime.now().now().time().strftime("%H:%M:%S")
            status = Status.objects.get(id=1)
            description = form["description"].value()
            ticket = Ticket(priority=priority, category=category, user=user, phone=phone,
                            date=date, time=time, description=description, department=department, status=status)
            ticket.save()

            return HttpResponseRedirect("user")
    else:
        form = AddNewTicket()

    return render(response, "support.html", {"form": form, "user": response.user})

@login_required(login_url='/login/')
def department(response):
    dp = Ticket.objects.all().order_by('-id')
    status = Status.objects.all()
    myFilter = OrderFilter(response.GET, queryset=dp)
    dp = myFilter.qs
    return render(response, "all_tickets.html",
                  {"dp": dp, "myFilter": myFilter, "status": status})

@login_required(login_url='/login/')
def user(response):
    name = Ticket.objects.filter(user=response.user.username).values()
    tickets = Ticket.objects.filter(user=response.user.get_full_name()).values().order_by('-id')
    return render(response, "user.html", {"name": name, "tickets": tickets})

@login_required(login_url='/login/')
def ticket(response, id):
    ticket = Ticket.objects.get(id=id)
    return render(response, "ticket.html", {"ticket": ticket})

@login_required(login_url='/login/')
def process(response, id):
    ticket = Ticket.objects.get(id=id)
    ticket.status = Status.objects.get(id=2).name
    ticket.save(update_fields=["status"])

    return HttpResponseRedirect("/tickets")

@login_required(login_url='/login/')
def complete(response, id):
    ticket = Ticket.objects.get(id=id)
    ticket.status = Status.objects.get(id=3).name
    ticket.save(update_fields=["status"])

    return HttpResponseRedirect("/tickets")
