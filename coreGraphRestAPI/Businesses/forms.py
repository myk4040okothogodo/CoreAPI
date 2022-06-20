from django_filters.rest_framework import BooleanFilter, FilterSet, DateFilter
from django.contrib.auth import get_user_model
from .models import Business

User = get_user_model()

class NullFilter(BooleanFilter):
    """Filter on a field set as null or not."""
    def filter(self, qs, value):
        if value is not None:
            return qs.filter(**{'%s__isnull' % self.name: value})
        return qs


class BusinessFilter(FilterSet):
    class Meta:
        model = Business
        fields = ('owner','name','business_address',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['owner'].extra.update(
            {'to_field_name': User.USERNAME_FIELD})
