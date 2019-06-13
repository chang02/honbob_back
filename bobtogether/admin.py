from django.contrib import admin

# Register your models here.
from .models import *

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'menu', 'location']

admin.site.register(Restaurant, RestaurantAdmin)