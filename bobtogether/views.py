from rest_framework import viewsets, permissions, generics
from .serializers import *
from .models import *

# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MatchingList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Matching.objects.all()
    serializer_class = MatchingSerializer

class MatchingDetails(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Matching.objects.all()
    serializer_class = MatchingSerializer

class MatchingRequestList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = MatchingRequest.objects.all()
    serializer_class = MatchingRequestSerializer

class MatchingDetails(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = MatchingRequest.objects.all()
    serializer_class = MatchingRequestSerializer

class ProfileList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetails(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
