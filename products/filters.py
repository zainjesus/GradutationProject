from django_filters import rest_framework as filters

from products.models import Product


class CharFiltersInFilter(filters.CharFilter, filters.BaseInFilter):
    pass


class HouseFilter(filters.FilterSet):
    type = CharFiltersInFilter(field_name='type__title', lookup_expr='in')
    price = filters.RangeFilter()
    square = filters.RangeFilter()
    area = filters.NumberFilter
    rooms = filters.NumberFilter
    floor = filters.NumberFilter

    class Meta:
        model = Product
        fields = ['type', 'price', 'area', 'rooms', 'square', 'floor']