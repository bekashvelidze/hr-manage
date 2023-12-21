from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Warehouse, Item, Type, Location
from .forms import CreateWarehouse, AddNewItem

# Create your views here.

def custom_404(request, exception):
    return render(request, 'main/404.html', status=404)


def index(response, id):
    wh = Warehouse.objects.get(id=id)
    return render(response, "main/base.html", {"wh": wh})


def home(response):
    deco_monitor = Item.objects.filter(type="მონიტორი", inventory_id=1)
    deco_case = Item.objects.filter(type="სისტემური ბლოკი", inventory_id=1)
    deco_laptops = Item.objects.filter(type="ლეპტოპი", inventory_id=1)
    deco_printer = Item.objects.filter(type="პრინტერი", inventory_id=1)
    deco_aio = Item.objects.filter(type="All In One", inventory_id=1)
    arch_monitor = Item.objects.filter(type="მონიტორი", inventory_id=2)
    arch_case = Item.objects.filter(type="სისტემური ბლოკი", inventory_id=2)
    arch_laptops = Item.objects.filter(type="ლეპტოპი", inventory_id=2)
    arch_printer = Item.objects.filter(type="პრინტერი", inventory_id=2)
    arch_aio = Item.objects.filter(type="All In One", inventory_id=2)
    return render(response, "main/home.html",
                  {"deco_monitor": deco_monitor, "deco_case": deco_case,
                   "arch_case": arch_case, "arch_monitor": arch_monitor,
                   "deco_laptops": deco_laptops, "arch_laptops": arch_laptops,
                   "deco_printer": deco_printer, "arch_printer": arch_printer,
                   "deco_aio": deco_aio, "arch_aio": arch_aio})


@login_required(login_url='/login/')
def warehouse(response, id):
    wh = Warehouse.objects.get(id=id)
    return render(response, "main/warehouse.html",
                  {"wh": wh})


@login_required(login_url='/login/')
def create(response):
    comp_id = {
        "დეკოლაინი": 1,
        "არქარეა": 2
        }
    if response.method == "POST":
        types = Type.objects
        locations = Location.objects
        companies = Warehouse.objects
        form = AddNewItem(response.POST, response.FILES)

        if form.is_valid():
            item_number = form["item_number"].value()
            type = types.get(id=int(form["type"].value()))
            owner = form["owner"].value()
            company = companies.get(id=int(form["company"].value()))
            description = form["description"].value()
            photo_url = form.cleaned_data.get("photo_url")
            location = locations.get(id=int(form["location"].value()))
            inventory_id = form["company"].value()
            item = Item(item_number=item_number, type=type, owner=owner, company=company,
                        description=description, photo_url=photo_url, location=location, inventory_id=inventory_id)
            item.save()
            return HttpResponseRedirect(f"/warehouse/{inventory_id}")
    else:
        form = AddNewItem()

    return render(response, "main/create.html", {"form": form, "comp_id": comp_id})


@login_required(login_url='/login/')
def item(response, id):
    item = Item.objects.get(item_number=id)
    return render(response, "main/item.html", {"item": item})
