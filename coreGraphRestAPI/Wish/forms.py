from django_filters.rest_framework import BooleanFilter, FilterSet, DateFilter
from django.contrib.auth import get_user_model
from .models import Wish

User = get_user_model()


class NullFilter(BooleanFilter):
    """Filter on a field set as null or not."""
    
    def filter(self, qs, value):
        if value is not None:
            return qs.filter(**{'%s__isnull' % self.name: value})
        return qs


class WishFilter(FilterSet):
    class Meta:
        model = Wish
        fields = ('created_at','products','user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['user'].extra.update(
                {'to_field_name': User.USERNAME_FIELD}
                )
