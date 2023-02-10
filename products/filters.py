from django_filters import rest_framework as filters

from products.models import House


class CharFiltersInFilter(filters.CharFilter, filters.BaseInFilter):
    pass


class HouseFilter(filters.FilterSet):
    category = CharFiltersInFilter(field_name='category__title', lookup_expr='in')
    price = filters.RangeFilter()

    class Meta:
        model = House
        fields = ['category', 'price']