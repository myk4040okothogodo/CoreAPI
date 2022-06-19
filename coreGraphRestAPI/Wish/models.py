from django.db import models
from coreGraphRestAPI.Products.models import Product
# Create your models here.


User = get_user_model()

class Wish(models.Model):
    user = models.OneToOneField(User, related_name="user_wish", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="products_wished")
    created_at = models.DateTimeField(auto_now_add=True)
