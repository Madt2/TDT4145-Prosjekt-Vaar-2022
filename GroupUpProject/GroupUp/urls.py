"""GroupUpProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from .views import UserDelete

# What does name= do??

urlpatterns = [
    path('front_page/', views.front_page, name='front_page'),
    path('groups_overview/', views.GroupsListView.as_view(),
         name='groups_overview_page'),
    path('groups_page/', views.MyGroupsListView.as_view(), name='groups_page'),
    path('group_page/<int:pk>', views.GroupDetailView.as_view(), name='group_page'),
    path('update_group/<int:pk>',
         views.UpdateGroupView.as_view(), name="update_group"),
    path('edit_group_page/', views.edit_group_page, name='edit_group_page'),
    path('group_matches/', views.group_matches_page),
    path('login/', views.login_page, name='login_page'),
    path('profile/', views.profile_page, name='profile_page'),
    path('new_group/', views.new_group_page, name='new_group_page'),
    path('register/', views.signup, name='signup_page'),
    path("age_error/", views.age_error, name='age_error'),
    path("delete_user/<int:pk>", views.UserDelete.as_view(), name='user_confirm_delete')
]
