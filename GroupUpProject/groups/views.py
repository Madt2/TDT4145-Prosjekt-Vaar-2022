from django.shortcuts import render
from models import Member, Group

# Create your views here.
def create_group_page(request):
    return render(request, "GroupUp/create_groups_page.html")

def mygroups(request):
    pass