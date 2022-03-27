from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .forms import GroupForm, SignUpForm, ProfileForm
from .models import Profile, Group, GroupReport, MemberOfGroup


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
        groups = Group.objects.all().exclude(group_leader_id=request.user.id)
        context = {'groups': groups}
        return render(request, 'GroupUp/groups_overview_page.html', context)


class GroupDetailView(DetailView):
    model = Group
    template_name = "GroupUp/group_page.html"
    pk_url_kwarg = 'pk'

    """
    def get(self, request, *args, **kwargs):
        context = {}
        context['members_of_group'] = MemberOfGroup.objects.filter(group_id=self.kwargs.get('pk'))
        for key, value in context.items():
            print (key, ' : ', value)
        return render(request, 'GroupUp/group_page.html', context)
        """

    def get_context_data(self, **kwargs):
        # Logic whether to display 'leave group' button.
        context = super().get_context_data(**kwargs)
        # Only contains an item if user is member of relevant group
        members_of_group = MemberOfGroup.objects.filter(group_id=self.kwargs.get('pk'),
                                                        member=self.request.user.profile)
        record_pk = list(MemberOfGroup.objects.filter(group_id=self.kwargs.get('pk'),
                                                             member=self.request.user.profile).values_list())
        # Need to check if queryset is empty, as indexing an empty list gives error
        if not record_pk:
            record_pk = 0
        else:
            record_pk = record_pk[0][0]
        print(record_pk)
        context['group_member'] = members_of_group
        context['record_pk'] = record_pk
        # Empties context if user is group leader
        if Group.objects.filter(id=self.kwargs.get('pk'), group_leader=self.request.user):
            context['group_member'] = MemberOfGroup.objects.none()
        for key, value in context.items():
            print(key, ' : ', value)
        return context


class MyGroupsListView(ListView):
    model = Group

    def get(self, request, *args, **kwargs):
        groups = Group.objects.filter(group_leader_id=request.user.id)
        context = {'groups': groups}
        return render(request, 'GroupUp/groups_page.html', context)


class UpdateGroupView(UpdateView):
    model = Group
    template_name = "GroupUp/update_group_page.html"
    fields = [
        "name",
        "description",
        "members",
        "interest",
        "image"
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


class ReportGroupPage(CreateView):
    model = GroupReport
    template_name = "GroupUp/report_group_page.html"
    pk_url_kwarg = 'pk'
    fields = '__all__'

    def get_success_url(self, **kwargs):
        return reverse("group_page", kwargs={'pk': self.object.pk})


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


class LeaveGroup(DeleteView):
    model = MemberOfGroup
    success_url = reverse_lazy('front_page')
    template_name = "GroupUp/leave_group_page.html"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record_pk'] = self.kwargs.get('pk')
        return context


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
