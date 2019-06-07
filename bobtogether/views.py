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
        req_sin = request.GET['since'] if 'since' in request.GET else '2001-01-01T00:00:00'
        req_til = request.GET['till'] if 'till' in request.GET else '2100-12-31T23:59:59'
        req_key = request.GET['keyword'] if 'keyword' in request.GET else ''
        
        # print(request.GET['gender'])
        if 'gender' in request.GET and int(request.GET['gender']) != 3:
            req_gen = [int(request.GET['gender']), 3]
        else:
            req_gen = [1, 2, 3]
        if 'status' in request.GET:
            req_status = [int(request.GET['status'])]
        else:
            req_status = [1, 2, 3]
        
        return queryset.filter(restaurant__name__icontains=req_res, matchingMessage__icontains=req_msg,
                                    maxNumber__lte=int(req_num), minage__gte=int(req_minage), maxage__lte=int(req_maxage),
                                    gender__in=req_gen, status__in=req_status,
                                    since__range=(req_sin, req_til), till__range=(req_sin, req_til), keyword__icontains=req_key)


class MatchingList(generics.ListAPIView):
    queryset = Matching.objects.all()
    serializer_class = MatchingRecursiveSerializer
    filter_backends = (MatchingFilterBackend,)
    filterset_fields = ('restaurant', 'matchingMessage', 'maxNumber',
                        'minage', 'maxage', 'gender', 'since', 'till')

class MatchingCreate(generics.CreateAPIView):
    queryset = Matching.objects.all()
    serializer_class = MatchingSerializer

class MatchingDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matching.objects.all()
    serializer_class = MatchingSerializer

class MatchingRequestList(generics.ListAPIView):
    queryset = MatchingRequest.objects.all()
    serializer_class = MatchingRequestRecursiveSerializer

class MatchingRequestCreate(generics.CreateAPIView):
    queryset = Matching.objects.all()
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
