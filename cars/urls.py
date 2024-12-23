from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cars.views import BrandModelViewSet, CardModelViewSet

router = DefaultRouter()
router.register('brands', BrandModelViewSet)
router.register('cars', CardModelViewSet)

urlpatterns = [
  path('', include(router.urls))
]
