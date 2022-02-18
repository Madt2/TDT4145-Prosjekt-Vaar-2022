from django.shortcuts import render
from django.http import HttpResponse

from .models import Profile, Group


# Create your views here.
def front_page(request):
    return render(request, "GroupUp/front_page.html")


def groups_overview_page(request):
    user_groups = Group.objects.all()
    user_groups.filter(user_groups.members, request.user)
    return render(request, "GroupUp/groups_overview_page.html", {'groups': user_groups})


def groups_page(request):
    user_group = Group.objects.all()
    user_group.filter(user_group.group_leader, request.user)
    return render(request, "GroupUp/groups_page.html", {'group': user_group})


def login_page(request):
    return render(request, "GroupUp/login/login_page.html")


def profile_page(request):
    return render(request, "GroupUp/profile_page.html")
