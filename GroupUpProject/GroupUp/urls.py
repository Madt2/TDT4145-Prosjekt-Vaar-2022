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

urlpatterns = [
    path('front_page/', views.front_page, name='front_page'),
    path('groups_overview/', views.groups_overview_page, name='groups_overview_page'),
    path('groups/', views.groups_page, name='groups_page'),
    path('login/', views.login_page, name='login_page'),
    path('profile/', views.profile_page, name='profile_page'),
    path('new_group/', views.new_group, name='new_group'),
]
