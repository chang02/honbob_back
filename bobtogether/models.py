from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField

STATUS = (
    (1, 'wait for matching'),
    (2, 'complete recruiting'),
    (3, 'complete meeting')
)

# Create your models here.
class Profile(models.Model):
    user = AutoOneToOneField(User, primary_key=True, on_delete=models.CASCADE, null=False)
    joined = models.DateTimeField(auto_now_add = True)
    name = models.TextField(default = '')
    GENDER = (
        (1, 'Male'),
        (2, 'Female'),
    )
    gender = models.PositiveIntegerField(choices=GENDER)
    age = models.PositiveIntegerField(default = 20)
    school = models.TextField(default = 'Seoul National University')
    major = models.TextField(default = '')
    description = models.TextField(default = '')
    contact = models.TextField(default = '010-0000-0000')

class Times(models.Model):
    mon = models.BigIntegerField(default = 0)
    tue = models.BigIntegerField(default = 0)
    wed = models.BigIntegerField(default = 0)
    thu = models.BigIntegerField(default = 0)
    fri = models.BigIntegerField(default = 0)
    sat = models.BigIntegerField(default = 0)
    sun = models.BigIntegerField(default = 0)

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    menu = models.TextField(default = '')
    location = models.TextField(default = '')
    times = AutoOneToOneField(Times, on_delete=models.CASCADE, null = False)

class Matching(models.Model):
    owner = models.ForeignKey(Profile, related_name='matchings', on_delete=models.CASCADE, null=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False)
    times = AutoOneToOneField(Times, on_delete=models.CASCADE, null = False)
    requestMessage = models.TextField(default = '')
    filter = models.TextField(default = '')
    totalNumber = models.PositiveIntegerField(default = 1)
    status = models.PositiveIntegerField(choices=STATUS)

class MatchingRequest(models.Model):
    user = models.ForeignKey(Profile, related_name='requests', on_delete=models.CASCADE, null=False)
    matching = models.ForeignKey(Matching, related_name='requests', on_delete=models.CASCADE, null=False)
    requestMessage = models.TextField(default = '')
    status = models.PositiveIntegerField(choices=STATUS)

class Notification(models.Model):
    user = models.ForeignKey(Profile, related_name='notifications', on_delete=models.CASCADE, null=False)
    matching = models.ForeignKey(Matching, on_delete=models.SET_NULL, null=True)
    message = models.TextField(default = '')
