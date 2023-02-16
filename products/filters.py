from django_filters import rest_framework as filters

from products.models import Product


class CharFiltersInFilter(filters.CharFilter, filters.BaseInFilter):
    pass


class HouseFilter(filters.FilterSet):
    type = filters.NumberFilter
    price = filters.RangeFilter()
    square = filters.RangeFilter()
    area = filters.NumberFilter
    rooms = filters.NumberFilter
    floor = filters.NumberFilter

    class Meta:
        model = Product
        fields = ['type', 'price', 'area', 'rooms', 'square', 'floor']