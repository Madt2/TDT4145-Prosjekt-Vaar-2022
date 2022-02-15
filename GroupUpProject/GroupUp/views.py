from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Profile


# Create your views here.
def front_page(request):
    return render(request, "GroupUp/front_page.html")


def groups_overview_page(request):
    return render(request, "GroupUp/groups_overview_page.html")


def groups_page(request):
    return render(request, "GroupUp/groups_page.html")


def login_page(request):
    return render(request, "GroupUp/login_page.html")


def profile_page(request):
    return render(request, "GroupUp/profile_page.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user, profile = form.save()
            login(request, user)
            return redirect('front_page')
    else:
        form = SignUpForm()
    return render(request, 'GroupUp/signup.html', {'form': form})


def profiles(request):
    profiles = User.objects.values().all()
    return render(request, "GroupUp/profiles_page.html", {'profiles': profiles})


def create_group(request):
    pass
