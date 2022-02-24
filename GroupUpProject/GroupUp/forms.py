from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from .models import Group, Profile, GroupReport


class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=True)
    # last_name = forms.CharField(max_length=30, required=True)
    # email = forms.EmailField(max_length=320, required=True)
    # date_of_birth = forms.DateField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'username',
            'email': 'E-mail',
            'password1': 'Password',
            'password2': 'Repeat Password',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}),
        }

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(SignUpForm, self).save(commit=True)
        # Changed to only make Users and not profiles for now
        # user_profile = Profile(user=user, age=self.cleaned_data['age'])
        # user_profile.save()
        return user  # user_profile


class GroupForm(ModelForm):
    # Removed image from fields and labels to attempt to successfully create group
    class Meta:
        model = Group
        fields = ['name', 'description', 'location', 'interests']
        labels = {
            'name': 'Name',
            'description': 'Group Description',
            'location': 'Location',
            'interests': 'Interests',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Group Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'interests': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Interests'}),
        }


"""
class ReportForm(ModelForm):
    class Meta:
        model = GroupReport
        fields = ['description', 'group']
        labels = {
            'group': 'Group',
            'description': 'Description',
        }
        widgets = {
            'group': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Reported Group'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'})
        }
"""


# Probably not necessary, as django has an authentication form built-in
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(),
            'password': forms.PasswordInput()
        }
