from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (ProductViewSet, ReviewCreateView, WishlistView, 
                   PromotionViewSet, CategoryListCreateView)

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'promotions', PromotionViewSet)

urlpatterns = [
    path('products/<int:product_id>/reviews/', 
         ReviewCreateView.as_view(), name='product-review'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
] + router.urls
