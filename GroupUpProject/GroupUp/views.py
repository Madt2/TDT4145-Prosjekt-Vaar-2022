from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormView

from .forms import GroupForm, SignUpForm, MatchForm
from .models import Profile, Group
from django.db.models import Q

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


class GroupsListView(ListView):
    model = Group

    def get(self, request, *args, **kwargs):
        groups = Group.objects.values().all().exclude(group_leader_id=request.user.id)
        context = {'groups': groups}
        return render(request, 'GroupUp/groups_overview_page.html', context)


class GroupDetailView(FormView, DetailView):
    model = Group
    template_name = "GroupUp/group_page.html"
    pk_url_kwarg = 'pk'
    form_class = MatchForm
    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        context["match_form"] = self.get_form()
        return context

    def get_form_kwargs(self):
        kwargs = super(GroupDetailView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = None
        return FormView.post(self, request, *args, **kwargs)

    def get_success_url(self):
        return reverse('front_page')

    def form_valid(self, form):
        print("do")
        user = self.request.user
        form.save(commit=False)
        liked_group= Group.objects.get(pk=self.kwargs.get('pk'))
        liked_by_group = Group.objects.get(group_leader=user)
        print("liked by group: ", liked_by_group)
        liked_group.likedBy.add(liked_by_group)
        liked_by_group.myLikes.add(liked_group)
        form.save_m2m()


        return super(GroupDetailView, self).form_valid(form)


class MyGroupsListView(ListView):
    model = Group

    def get(self, request, *args, **kwargs):
        # profile = Profile.objects.get(pk=request.user.id)
        # print("Profile: ", profile)
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

class MatchedGroupsListView(ListView):
    model = Group

    def get(self, request, *args, **kwargs):
        groups = Group.objects.values().all()
        context = {'groups': groups}
        return render(request, 'GroupUp/group_matches_page.html', context)

def group_matches_page(request):
    # Fix so that only matched groups are shown, not all
    groups = Group.objects.values().all()
    context = {'groups': groups}
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
    user = request.user
    # Not sure how to send single object instead of list into a html file
    # Seems as though the argument in render has to be a dict
    users = [user]
    return render(request, "GroupUp/profile_page.html", {'users': users})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user, profile = form.save()
            login(request, user)
            return redirect('front_page')
        else:
            return render(request, "GroupUp/age_error_page.html", {'errors' : form.errors})
    return redirect('login_page')

def age_error(request):
    return render(request, "GroupUp/age_error_page.html")