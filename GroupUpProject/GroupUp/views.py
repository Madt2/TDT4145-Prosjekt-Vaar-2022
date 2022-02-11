from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm


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
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('front_page')
    else:
        form = SignUpForm()
    return render(request, 'GroupUp/signup.html', {'form': form})
