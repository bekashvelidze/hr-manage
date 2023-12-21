from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path("support", views.support, name="support"),
    path("tickets", views.department, name="department"),
    path("user", views.user, name="user"),
    path("ticket/<int:id>", views.ticket, name="ticket"),
    path("process/<int:id>", views.process, name="process"),
    path("complete/<int:id>", views.complete, name="complete")
]
