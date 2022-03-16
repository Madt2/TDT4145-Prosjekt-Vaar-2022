from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from .models import Group, Profile, GroupReport, Image
import datetime


class SignUpForm(UserCreationForm):
    def year_choices():
        return [r for r in range(1950, datetime.date.today().year + 1)]

    DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')

    first_name = forms.CharField(
        max_length=30, required=True)
    last_name = forms.CharField(
        max_length=30, required=True)
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.', required=True)
    date_of_birth = forms.DateField(
        required=True, input_formats=DATE_INPUT_FORMATS, widget=forms.SelectDateWidget(years=year_choices()))
    description = forms.CharField(
        max_length=300, help_text='Optional.', required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'description',
                  'email', 'date_of_birth', 'password1', 'password2',)

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        age = (datetime.date.today() - date_of_birth).days / 365
        if age < 18:
            raise forms.ValidationError("You need to be 18 or above to register a user")
        return date_of_birth

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError(
                "Can't create User and UserProfile without database save")
        user = super(SignUpForm, self).save(commit=True)
        user_profile = Profile(user=user, first_name=self.cleaned_data['first_name'],
                               last_name=self.cleaned_data['last_name'],
                               email=self.cleaned_data['email'], date_of_birth=self.cleaned_data['date_of_birth'],
                               description=self.cleaned_data['description'])
        user_profile.save()
        return user, user_profile


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'group_leader',
                  'members', 'location', 'description', 'interest')
        labels = {
            'name': '',
            'members': 'Members',
            'location': 'Location',
            'description': 'Group Description',
            'image': 'Group Image',
            'interest': "Interest"
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                           'style': 'max-width: 500px;',
                                           'placeholder': 'Group Name'}),
            # 'activity_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Activity'}),
            # 'activity_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Activity Date'}),
            'members': forms.SelectMultiple(attrs={'class': 'form-control',
                                                   'style': 'max-width: 500px;',
                                                   'placeholder': 'Members'}),
            'location': forms.TextInput(attrs={'class': 'form-control',
                                               'style': 'max-width: 500px;',
                                               'placeholder': 'Trondheim'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'style': 'max-width: 500px;', 'rows': '3',
                                                 'placeholder': 'Description'}),
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


class ImageForm(forms.ModelForm):
    """Form for the image model"""

    class Meta:
        model = Image
        fields = ('title', 'image')
