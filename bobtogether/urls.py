from django.urls import path
from bobtogether import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profile/<int:pk>/', views.ProfileDetails.as_view()),
    path('profile/self/', views.ProfileCurrent.as_view()),
    path('restaurants/', views.RestaurantList.as_view()),
    path('restaurant/<int:pk>/', views.RestaurantDetails.as_view()),
    path('matchings/', views.MatchingList.as_view()),
    path('matching/<int:pk>/', views.MatchingDetails.as_view()),
    path('requests/', views.MatchingRequestList.as_view()),
    path('request/<int:pk>/', views.MatchingRequestDetails.as_view()),
    path('notification/<int:pk>/', views.NotificationDetails.as_view())
]
