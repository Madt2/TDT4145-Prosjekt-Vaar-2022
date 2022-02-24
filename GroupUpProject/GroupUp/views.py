from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView

from .forms import GroupForm, SignUpForm
from .models import Profile, Group


# Create your views here.
def front_page(request):
    return render(request, "GroupUp/front_page.html")


def new_group_page(request):
    if request.method == 'POST':
        form = GroupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('front_page')
    else:
        form = GroupForm()
    return render(request, 'GroupUp/new_group.html', {'form': form})


def groups_overview_page(request):
    # Temporarily disabled logic
    # user_groups = Group.objects.all()
    # user_groups.filter(user_groups.members, request.user)
    all_groups = Group.objects.all()
    return render(request, "GroupUp/groups_overview_page.html", {"groups": all_groups})


class MyGroupsListView(ListView):
    model = Group

    def get(self, request, *args, **kwargs):
        groups = Group.objects.values().filter(group_leader_id=request.user.id)
        context = {'groups': groups}
        return render(request, 'GroupUp/groups_page.html', context)



def group_page(request):
    # Temporarily disabled logic
    # user_group = Group.objects.all()
    # user_group.filter(user_group.group_leader, request.user)
    return render(request, "GroupUp/group_page.html")


def edit_group_page(request):
    # Temporarily disabled logic
    # user_group = Group.objects.all()
    # user_group.filter(user_group.group_leader, request.user)
    return render(request, "GroupUp/edit_group_page.html")


def login_page(request):
    login_form = AuthenticationForm()
    signup_form = SignUpForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('front_page')

    return render(request, 'GroupUp/login_page.html', {'login_form': login_form, "signup_form": signup_form})


def profile_page(request):
    user = request.user
    # Not sure how to send single object instead of list into a html file
    # Seems as though the argument in render has to be a dict
    users = [user]
    return render(request, "GroupUp/profile_page.html", {'users': users})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            # Changed temporarily to only save Users and not profiles
            user, profile = form.save()
            login(request, user)
            return redirect('front_page')
    return redirect('login_page')
