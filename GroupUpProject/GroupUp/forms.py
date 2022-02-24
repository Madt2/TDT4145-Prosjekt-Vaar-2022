from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Group, Profile
import datetime


class SignUpForm(UserCreationForm):
    def year_choices():
        return [r for r in range(1984, datetime.date.today().year+1)]
    DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')
    
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')
    date_of_birth = forms.DateField(required=True, input_formats=DATE_INPUT_FORMATS, widget=forms.SelectDateWidget(years=year_choices()))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'date_of_birth', 'password1', 'password2', )

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError(
                "Can't create User and UserProfile without database save")
        user = super(SignUpForm, self).save(commit=True)
        user_profile = Profile(user=user, first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'], 
                                email=self.cleaned_data['email'], date_of_birth=self.cleaned_data['date_of_birth'])
        user_profile.save()
        return user, user_profile


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'owner', 'activity_name', 'activity_date',
                  'members', 'location', 'description', 'image')
        labels = {
            'name': '',
            'activity_name': 'Activity',
            'activity_date': 'YYYY-MM-DD HH:MM:SS',
            'members': 'Members',
            'location': 'Location',
            'description': 'Group Description',
            'image': 'Group Image'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Group Name'}),
            'activity_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Activity'}),
            'activity_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Activity Date'}),
            'members': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Members'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Trondheim'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }
