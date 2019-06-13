from django.contrib import admin

# Register your models here.
from .models import *

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'menu', 'location']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name']

class MatchingAdmin(admin.ModelAdmin):
    list_display = ['owner', 'matchingMessage']

class MatchingRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'matching']

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'message']

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Matching, MatchingAdmin)
admin.site.register(MatchingRequest, MatchingRequestAdmin)
admin.site.register(Notification, NotificationAdmin)