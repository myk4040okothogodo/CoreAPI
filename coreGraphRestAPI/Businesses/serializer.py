from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import ImageUpload, BusinessImage, BusinessComment, BusinessAddress, Business
from drf_writable_nested import WritableNestedModelSerializer


User = get_user_model()





class BusinessCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessComment
        fields = "__all__"

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = "__all__"

class BusinessImageSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
      image  = ImageUploadSerializer(read_only = False)
      class Meta:
          model = BusinessImage
          fields = ('image', 'is_cover')

class BusinessAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessAddress
        fields = "__all__"

class BusinessSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    business_address = BusinessAddressSerializer(read_only = False)
    business_comments = BusinessCommentSerializer(read_only = False)
    business_images  = BusinessImageSerializer(read_only = False)
    class Meta:
        model = Business
        fields = ['id','owner','name','business_address','business_comments','business_images','links']

    def get_links(self, obj):
        request = self.context['request']
        links = {
                'self': reverse('business-detail',
                kwargs = {'pk': obj.pk}, request=request),
                'products': None,
                }
        return links
