from django.contrib import admin

# Register your models here.
from .models import Profile, GroupReport

admin.site.register(Profile)
admin.site.register(GroupReport)