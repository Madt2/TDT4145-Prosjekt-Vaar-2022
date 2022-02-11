from django.db import models
from django.contrib.auth import get_user_model

class Member(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Group(models.Model):
    group_name = models.CharField(max_length=30)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    members = models.ManyToManyField(
        Member,
        through_fields=('group', 'member'),
    )
    activity_name = models.CharField(max_length=100)
    activity_date = models.DateField()
    description = models.TextField()
    
    def __str__(self):
        return self.group_name
