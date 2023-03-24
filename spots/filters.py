import django_filters
from .models import SurfSpots

class SpotFilter(django_filters.FilterSet):
    class Meta:
        model = SurfSpots
        fields = ['level']