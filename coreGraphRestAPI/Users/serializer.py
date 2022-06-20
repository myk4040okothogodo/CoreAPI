from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import UserProfile, UserAddress, ImageUpload
from drf_writable_nested import WritableNestedModelSerializer



User = get_user_model()


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ('image',)


class UserProfileSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    profile_picture = ImageUploadSerializer(read_only = False)
    class Meta:
        model = UserProfile
        fields = ('profile_picture','dob','phone','country_code')


class UserAddressSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user_profile = UserProfileSerializer(read_only = False)
        
    class Meta:
        model = UserAddress
        fields = ('user_profile','street','city','state','country','is_default')



class UserSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    user_address = UserAddressSerializer(read_only=False)
    
    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD,'email','password','first_name','last_name','user_address','is_active','links')


    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()

        return {
                'self': reverse('user-detail',
                kwargs = {User.USERNAME_FIELD: username}, request=request),
                }

    

