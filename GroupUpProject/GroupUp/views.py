from django.shortcuts import render
from django.http import HttpResponse


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


def new_group(request):
    return render(request, "GroupUp/new_group.html")
