from django.urls import path, include
from rest_framework import routers
from bobtogether import views

router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)

urlpatterns = [
    path('', include(router.urls))
]