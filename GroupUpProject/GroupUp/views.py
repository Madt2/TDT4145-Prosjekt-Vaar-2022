from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import LoginForm
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
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('front_page')
    else:
        form = AuthenticationForm()
    return render(request, 'GroupUp/login_page.html', {'form': form})


def profile_page(request):
    return render(request, "GroupUp/profile_page.html")
