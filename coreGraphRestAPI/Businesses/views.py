from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, filters
from .serializer import BusinessSerializer
from .models import Business
from .forms import  BusinessFilter
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


class BusinessViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing Businesses."""    
    queryset = Business.objects.order_by('name') 
    serializer_class = BusinessSerializer
    filter_class = BusinessFilter
    search_fields = ('owner','name','business_address')
    ordering_fields = ('name','business_address')
