from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, filters
from .serializer import WishSerializer
from .models import Wish
from .forms import WishFilter
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering and pagination."""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
            )
    permission_classes = (
        permissions.IsAuthenticated,
        #TokenHasReadWriteScope,
        )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
            )    


class WishViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing Wishes."""
    queryset = Wish.objects.order_by('created_at') 
    serializer_class = WishSerializer 
    filter_class = WishFilter
    search_fields = ('created_at','user','products')
    ordering_fields = ('created_at','user')
