from django.db import models
from django.contrib.auth import get_user_model
from annoying.fields import AutoOneToOneField
from datetime import datetime

# Create your models here.
User = get_user_model()

class Profile(models.Model):
    user = AutoOneToOneField(User, primary_key=True, on_delete=models.CASCADE, null=False)
    joined = models.DateTimeField(auto_now_add = True)
    name = models.CharField(default = '', max_length = 30)
    GENDER = (
        (1, 'Male'),
        (2, 'Female'),
    )
    gender = models.PositiveIntegerField(choices=GENDER, default = 1)
    age = models.PositiveIntegerField(default = 20)
    school = models.CharField(default = 'Seoul National University', max_length = 50)
    major = models.CharField(default = '', max_length = 30)
    description = models.TextField(default = '')
    contact = models.TextField(default = '010-0000-0000')

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    menu = models.TextField(default = '')
    location = models.TextField(default = '')
    hours = models.TextField(default = '')

class Matching(models.Model):
    owner = models.ForeignKey(Profile, related_name='matchings', on_delete=models.CASCADE, null=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False)
    since = models.DateTimeField(default = datetime.now)
    till = models.DateTimeField(default = datetime.now)
    minage = models.PositiveIntegerField(default = 20)
    maxage = models.PositiveIntegerField(default = 30)
    GENDER = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Any')
    )
    gender = models.PositiveIntegerField(choices=GENDER, default = 1)
    matchingMessage = models.TextField(default = '')
    keyword = models.TextField(default = '')
    maxNumber = models.PositiveIntegerField(default = 2)
    STATUS = (
        (1, '모집중'),
        (2, '모집 완료'),
        (3, '만남 완료')
    )
    status = models.PositiveIntegerField(choices=STATUS, default=1)

class MatchingRequest(models.Model):
    user = models.ForeignKey(Profile, related_name='requests', on_delete=models.CASCADE, null=False)
    matching = models.ForeignKey(Matching, related_name='requests', on_delete=models.CASCADE, null=False)
    requestMessage = models.TextField(default = '')
    STATUS = (
        (1, '수락 대기중'),
        (2, '수락됨'),
    )
    status = models.PositiveIntegerField(choices=STATUS, default=1)

class Notification(models.Model):
    user = models.ForeignKey(Profile, related_name='notifications', on_delete=models.CASCADE, null=False)
    matching = models.ForeignKey(Matching, on_delete=models.SET_NULL, null=True)
    message = models.TextField(default = '')

class MatchingReview(models.Model):
    user = models.ForeignKey(Profile, related_name='reviews', on_delete=models.CASCADE, null=False)
    matching = models.ForeignKey(Matching, on_delete=models.CASCADE, null=True)
    score = models.PositiveSmallIntegerField(default = 3) # 1 ~ 5
    title = models.CharField(default = '', max_length = 30)
    detail = models.TextField(default = '')
