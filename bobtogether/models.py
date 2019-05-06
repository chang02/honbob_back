from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    menu = models.TextField()
    location = models.TextField()
    openTime = models.TimeField()
    closeTime = models.TimeField()


class Matching(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False)
    diningTime = models.DateTimeField()
    requestMessage = models.TextField()

    GENDER = (
        (1, 'Male'),
        (2, 'Female'),
    )
    preferGender = models.PositiveIntegerField(choices=GENDER)
    totalNumber = models.PositiveIntegerField()

    STATUS = (
        (1, 'wait for matching'),
        (2, 'complete recruiting'),
        (3, 'complete meeting')
    )
    status = models.PositiveIntegerField(choices=STATUS)