from rest_framework import viewsets, permissions
from .serializers import *
from .models import *

# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

  queryset = Restaurant.objects.all()
  serializer_class = RestaurantSerializer