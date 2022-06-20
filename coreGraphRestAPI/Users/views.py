from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, filters
from .serializer import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend



from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


User = get_user_model()


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
    
class UserViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing users."""
    
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD) 
    serializer_class = UserSerializer   
