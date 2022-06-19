from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product, ProductImage, ProductComment, Category, ImageUpload
from drf_writable_nested import WritableNestedModelSerializer


User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = "__all__"


class ProductImageSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    image = ImageUploadSerializer(read_only = False)
    class Meta:
        model = ProductImage
        fields = "__all__"

class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = "__all__"


class ProductSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    category = CategorySerializer(read_only = False)
    product_images = ProductImageSerializer(read_only = False)
    product_comments = ProductCommentSerializer(read_only = False)
    class Meta:
        model = Product
        fields = ['id','category','business','name','price','total_available','total_count','description','product_images','product_comments','links']

    def get_links(self, obj):
        request = self.context['request']
        links = {
                'self': reverse('product-detail',
                kwargs = {'pk': obj.pk}, request=request),
                'businesses': None,
                }

        if obj.business:
            links['businesses'] = reverse('business-detail',
                kwargs = {'pk': obj.business_id}, request=request)        
        return links




