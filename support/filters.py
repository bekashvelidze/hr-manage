import django_filters

from .models import Ticket

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Ticket
        fields = ['status', 'priority', 'category']
