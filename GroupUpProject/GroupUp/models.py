from datetime import date
from pydoc import describe
from django.db import models
import uuid
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default="", max_length=30)
    last_name = models.CharField(default="", max_length=30)
    email = models.EmailField("User's e-mail")
    date_of_birth = models.DateField("User's birth date")
    description = models.TextField(default="", blank=True)
    profile_picture = models.ImageField(null=True, blank=True, default='GroupUp/users_pictures/profile.jpg')

    def age(self):
        today = date.today()
        born = self.date_of_birth
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name

    def __meta__(self):
        db_table = 'GroupUp_profile'

    def get_all_objects(self):
        all_entries = Profile.objects.all()
        return all_entries

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Interest(models.Model):
    name = models.CharField("NameOfInterest", max_length=30)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField('Group Name', max_length=120)
    group_leader = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField("Description", blank=True)
    members = models.ManyToManyField(
        Profile, through="MemberOfGroup", blank=True)
    location = models.CharField("Location", max_length=30)
    interest = models.ForeignKey(
        Interest, blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField("GroupImage")

    objects = models.Manager()

    def __meta__(self):
        db_table = 'GroupUp_group'

    def __str__(self):
        return self.name

    # Veldig dårlig kode, dette må fikses
    def get_age_range(self):
        members = self.members.all()
        min_age = 100
        max_age = 0
        for member in members:
            if member.age() > max_age:
                max_age = member.age()
            if member.age() < min_age:
                min_age = member.age()
        return {"min_age": min_age, "max_age": max_age}

    def get_group_leader(self):
        return Profile.objects.filter(user_id=self.group_leader).first()

    @property
    def numberOfMembers(self):
        return self.members.count()


class GroupReport(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.group


class MemberOfGroup(models.Model):
    member = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
