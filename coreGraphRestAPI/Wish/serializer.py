from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Wish



User = get_user_model()


class WishSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    class Meta:
        model = Wish
        fields = ['id','user','products','links']

    def get_links(self, obj):
        request = self.context['request']
        links = {
                'self': reverse('wish-detail',
                kwargs = {'pk': obj.pk}, request=request),
                'shopper': None,
                'items': None,
                }
        if obj.user_id:
            links['shopper'] = reverse('user-detail',
            kwargs = {User.USERNAME_FIELD: obj.user_id}, request=request)

        if obj.products:
            links['items'] = reverse('product-detail',
            kwargs = {'pk': obj.products}, request=request)
         
        return links

