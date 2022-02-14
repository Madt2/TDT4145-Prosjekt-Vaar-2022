from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Interests(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    picture = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length= 50, primary_key= True)
    description = models.TextField()
    picture = models.ImageField()
    average_age = models.IntegerField()
    location = models.CharField(max_length= 30)
    date = models.DateTimeField(default=timezone.now)
    members = models.ManyToManyField(User, through="GroupMembers", blank=False)
    interests = models.ManyToManyField(Interests)

    def __str__(self):
        return self.name

class GroupMembers(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField()

class GroupMatches(models.Model):
    review = models.IntegerField()

class Reports(models.Model):
    report_type = models.CharField(max_length=20)
    description = models.TextField()
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)



