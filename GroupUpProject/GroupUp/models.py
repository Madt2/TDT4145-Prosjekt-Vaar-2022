from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #username = models.CharField(user.username)
    first_name = models.CharField(default="", max_length=30)
    last_name = models.CharField(default="", max_length=30)
    email = models.EmailField('User Email')
    age = models.IntegerField()

    def __meta__(self):
        db_table = 'GroupUp_profile'

    def get_all_objects(self):
        all_entries = Profile.objects.all()
        return all_entries

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Interest(models.Model):
    name = models.CharField(max_length=30)


class Group(models.Model):
    name = models.CharField('Event Name', max_length=120)
    activity_name = models.CharField('Activity', max_length=120)
    activity_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(
        Profile, through="MemberOfGroup", blank=True)
    location = models.CharField(max_length=30)
    interests = models.ManyToManyField(Interest)
    image = models.CharField(max_length=100)

    objects = models.Manager()

    def __meta__(self):
        db_table = 'GroupUp_group'

    def get_owner_group(self):
        all_entries = Group.objects.all()
        return all_entries

    def __str__(self):
        return self.name


class MemberOfGroup(models.Model):
    member = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Report(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
