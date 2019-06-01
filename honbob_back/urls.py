from django.contrib import admin, auth
from django.urls import path, include

urlpatterns = [
    path('', include('bobtogether.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
]
