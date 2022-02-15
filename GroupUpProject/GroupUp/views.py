from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignUpForm, GroupForm
from .models import Profile, Group
from django.views.generic.detail import DetailView


# Create your views here.
def front_page(request):
    return render(request, "GroupUp/front_page.html")


class GroupDetailView(DetailView):
    model = Group

    def get(self, request, *args, **kwargs):
        groups = Group.objects.values().filter(owner_id=request.user.id)
        print(request.user.id)
        print(groups[0])
        #group = get_object_or_404(Group, pk=kwargs['pk'])
        context = {'groups': groups}
        return render(request, 'GroupUp/groups_page.html', context)


def groups_overview_page(request):
    return render(request, "GroupUp/groups_overview_page.html")


def groups_page(request):
    my_group = Group.object.all()
    my_group.filter(my_group.owner, request.user)
    return render(request, "GroupUp/groups_page.html", {'group': my_group})


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
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('front_page')
    else:
        form = GroupForm()
    return render(request, 'GroupUp/create_group_page.html', {'form': form})
