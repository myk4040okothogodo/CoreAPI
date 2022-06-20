from django.db import models
from coreGraphRestAPI.Products.models import Product
from django.contrib.auth import get_user_model


User = get_user_model()

class Cart(models.Model):
    product = models.ForeignKey(Product, related_name="product_carts", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_carts", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.user.email}"

    class Meta:
        ordering = ("-created_at",)



