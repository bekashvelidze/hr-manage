from django.urls import path
from .views import views

urlpatterns = [
    path("schedule", views.schedule, name="schedule")
]
