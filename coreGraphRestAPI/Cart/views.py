from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, filters
from .serializer import CartSerializer
from .models import Cart
from .forms import CartFilter
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


class CartViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing Carts."""
    
    queryset = Cart.objects.order_by('created_at') 
    serializer_class = CartSerializer 
    filter_class = CartFilter
    search_fields = ('created_at','user','quantity','product')
    ordering_fields = ('created_at','quantity','user')
