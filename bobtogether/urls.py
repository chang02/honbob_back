from django.urls import path
from bobtogether import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetails.as_view()),
    path('profiles/', views.ProfileList.as_view()),
    path('profile/<int:pk>/', views.ProfileDetails.as_view()),
    path('profile/self/', views.ProfileCurrent.as_view()),
    path('restaurants/', views.RestaurantList.as_view()),
    path('restaurant/<int:pk>/', views.RestaurantDetails.as_view()),
    path('matchings/', views.MatchingList.as_view()),
    path('matching/', views.MatchingCreate.as_view()),
    path('matching/<int:pk>/', views.MatchingDetails.as_view()),
    path('requests/', views.MatchingRequestList.as_view()),
    path('request/', views.MatchingRequestCreate.as_view()),
    path('request/<int:pk>/', views.MatchingRequestDetails.as_view()),
    path('notification/<int:pk>/', views.NotificationDetails.as_view())
]
