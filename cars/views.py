from dj_rql.drf import RQLFilterBackend
from rest_framework import viewsets, permissions
from cars.models import Brand, Car
from cars.filters import BrandFilterClass, CarFilterClass
from cars.serializers import BrandModelSerializer, CardModelSerializer
from cars.permissions import CarOwnerPermission

class BrandModelViewSet(viewsets.ModelViewSet):
  queryset = Brand.objects.all()
  serializer_class = BrandModelSerializer
  filter_backends = [RQLFilterBackend]
  rql_filter_class = BrandFilterClass
  permission_classes = [permissions.AllowAny]
  
class CardModelViewSet(viewsets.ModelViewSet):
  queryset = Car.objects.all()
  serializer_class = CardModelSerializer
  filter_backends = [RQLFilterBackend]
  rql_filter_class = CarFilterClass
  
  permission_classes = [permissions.DjangoModelPermissions, CarOwnerPermission]


  