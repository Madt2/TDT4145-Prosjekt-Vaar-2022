from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .forms import GroupForm, SignUpForm, ProfileForm
from .models import Profile, Group


# Create your views here.
def front_page(request):
    return render(request, "GroupUp/front_page.html")


def new_group_page(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('front_page')
    else:
        form = GroupForm()
    return render(request, 'GroupUp/new_group.html', {'form': form})


class GroupsListView(ListView):
    model = Group

    def get(self, request, *args, **kwargs):
        groups = Group.objects.values().all().exclude(group_leader_id=request.user.id)
        context = {'groups': groups}
        return render(request, 'GroupUp/groups_overview_page.html', context)


class GroupDetailView(DetailView):
    model = Group
    template_name = "GroupUp/group_page.html"
    pk_url_kwarg = 'pk'


class MyGroupsListView(ListView):
    model = Group

    def get(self, request, *args, **kwargs):
        groups = Group.objects.values().filter(group_leader_id=request.user.id)
        context = {'groups': groups}
        return render(request, 'GroupUp/groups_page.html', context)


class UpdateGroupView(UpdateView):
    model = Group
    template_name = "GroupUp/update_group_page.html"
    fields = [
        "name",
        "description",
        "members",
        "interest"
    ]

    def get_success_url(self, **kwargs):
        return reverse("group_page", kwargs={'pk': self.object.pk})


def group_page(request):
    # Temporarily disabled logic
    # user_group = Group.objects.all()
    # user_group.filter(user_group.group_leader, request.user)
    return render(request, "GroupUp/group_page.html")


def group_matches_page(request):
    # Temporarily disabled logic
    # user_group = Group.objects.all()
    # user_group.filter(user_group.group_leader, request.user)
    return render(request, "GroupUp/group_matches_page.html")


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
    profile = request.user.profile
    # Not sure how to send single object instead of list into a html file
    # Seems as though the argument in render has to be a dict
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, "GroupUp/profile_page.html", context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user, profile = form.save()
            login(request, user)
            return redirect('front_page')
        else:
            return render(request, "GroupUp/age_error_page.html", {'errors': form.errors})
    return redirect('login_page')


def age_error(request):
    return render(request, "GroupUp/age_error_page.html")


'''def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'GroupUp/profile_page.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'GroupUp/profile_page.html', {'form': form})'''
