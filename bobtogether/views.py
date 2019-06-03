from rest_framework import permissions, generics, mixins
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
# import pandas as pd

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RestaurantFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        req_name = request.GET['name'] if 'name' in request.GET else ''
        req_dsp = request.GET['description'] if 'description' in request.GET else ''
        req_menu = request.GET['menu'] if 'menu' in request.GET else ''
        req_loc = request.GET['location'] if 'location' in request.GET else ''
        return queryset.filter(name__icontains=req_name, description__icontains=req_dsp,
                               menu__icontains=req_menu, location__icontains=req_loc)

class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = (RestaurantFilterBackend,)
    filterset_fields = ('name', 'description', 'menu', 'location')

class RestaurantDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MatchingFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        req_res = request.GET['restaurant'] if 'restaurant' in request.GET else ''
        req_msg = request.GET['matchingMessage'] if 'matchingMessage' in request.GET else ''
        req_num = request.GET['maxNumber'] if 'maxNumber' in request.GET else 100
        req_minage = request.GET['minage'] if 'minage' in request.GET else 0
        req_maxage = request.GET['maxage'] if 'maxage' in request.GET else 100
        req_sin = request.GET['since'] if 'since' in request.GET else '2019-06-05T14:00:00'
        req_til = request.GET['till'] if 'till' in request.GET else '2020-01-01T00:00:00'

        if 'gender' in request.GET:
            req_gen = request.GET['gender']
            return queryset.filter(restaurant__name__icontains=req_res, matchingMessage__icontains=req_msg,
                                maxNumber__lte=int(req_num), minage__gte=int(req_minage), maxage__lte=int(req_maxage),
                                gender=int(req_gen),
                                since__range=(req_sin, req_til), till__range=(req_sin, req_til))
        else:
            return queryset.filter(restaurant__name__icontains=req_res, matchingMessage__icontains=req_msg,
                                maxNumber__lte=int(req_num), minage__gte=int(req_minage), maxage__lte=int(req_maxage),
                                since__range=(req_sin, req_til), till__range=(req_sin, req_til))


class MatchingList(generics.ListCreateAPIView):
    queryset = Matching.objects.all()
    serializer_class = MatchingSerializer
    filter_backends = (MatchingFilterBackend,)
    filterset_fields = ('restaurant', 'matchingMessage', 'number',
                        'age', 'gender', 'since', 'utill')

class MatchingDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matching.objects.all()
    serializer_class = MatchingSerializer

class MatchingRequestList(generics.ListCreateAPIView):
    queryset = MatchingRequest.objects.all()
    serializer_class = MatchingRequestSerializer

class MatchingRequestDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = MatchingRequest.objects.all()
    serializer_class = MatchingRequestSerializer

class MatchingReviewList(generics.ListCreateAPIView):
    queryset = MatchingReview.objects.all()
    serializer_class = MatchingReviewSerializer

class MatchingReviewDetails(generics.RetrieveUpdateAPIView):
    queryset = MatchingReview.objects.all()
    serializer_class = MatchingReviewSerializer

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetails(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileCurrent(generics.GenericAPIView):
    def get(self, request, format = None):
        if request.user.is_authenticated:
            return Response(ProfileSerializer(request.user.profile).data)
        else:
            raise PermissionDenied('Not logged in.')

class NotificationDetails(generics.RetrieveDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
