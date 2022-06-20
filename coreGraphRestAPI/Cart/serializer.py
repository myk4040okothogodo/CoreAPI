from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Cart



User = get_user_model()


class CartSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    class Meta:
        model = Cart
        fields = ['id','product','user','quantity','links']

    def get_links(self, obj):
        request = self.context['request']
        links = {
                'self': reverse('cart-detail',
                kwargs = {'pk': obj.pk}, request=request),
                'shopper': None,
                'purchases': None,
                }
        if obj.user_id:
            links['shopper'] = reverse('user-detail',
            kwargs = {User.USERNAME_FIELD: obj.user_id}, request=request)
        if obj.product:
            links['purchases'] = reverse('product-detail',
            kwargs = {'pk': obj.product}, request=request)
         
        return links

