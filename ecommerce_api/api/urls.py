from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CustomerViewSet, refresh_data

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('refresh/', refresh_data),
]
