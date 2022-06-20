from django.db import models
from coreGraphRestAPI.Users.models import ImageUpload
from django.contrib.auth import get_user_model

User = get_user_model()


class BusinessImage(models.Model):
    image = models.ForeignKey(ImageUpload, related_name="image_business", on_delete=models.CASCADE)
    is_cover = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.image}"


class BusinessComment(models.Model):
    user = models.ForeignKey(User, related_name="user_comments_on_business", on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)


class BusinessAddress(models.Model):
    street = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="Kenya")
    is_default = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.street  


class Business(models.Model):
    owner = models.OneToOneField(User, related_name="business_owner", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    business_address = models.ForeignKey(BusinessAddress, related_name="business_address", on_delete=models.CASCADE)
    business_comments = models.ForeignKey(BusinessComment, related_name="business_comments", on_delete=models.CASCADE)
    business_images = models.ForeignKey(BusinessImage, related_name="business_images", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

