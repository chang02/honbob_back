from bobtogether.models import *
from rest_framework import serializers

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'description', 'menu', 'location', 'openTime', 'closeTime')