from rest_framework.routers import DefaultRouter
from .Users.views import UserViewSet
from .Products.views import ProductViewSet
from .Businesses.views import BusinessViewSet
from .Cart.views import  CartViewSet
from .Wish.views import  WishViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'businesses',BusinessViewSet)
router.register(r'carts', CartViewSet)
router.register(r'wishes', WishViewSet)
