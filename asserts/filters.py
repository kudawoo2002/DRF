import django_filters
from .models import Assert

class AssertFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(field_name='department', lookup_expr='iexact')
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')
    id = django_filters.RangeFilter(field_name='id')

    class Meta:
        model = Assert
        fields = ['department', 'name', 'id']