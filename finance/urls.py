from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path("addloan", views.addloan, name="addloan"),
    path("myloans", views.myloans, name="myloans"),
    path("loan/<int:id>", views.loan, name="loan"),
    path("pay", views.pay, name="pay")
]