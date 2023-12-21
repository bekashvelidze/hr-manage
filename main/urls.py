from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.item, name="item"),
    path("", views.home, name="home"),
    path("create", views.create, name="create"),
    path("warehouse/<int:id>", views.warehouse, name="warehouse"),
]
