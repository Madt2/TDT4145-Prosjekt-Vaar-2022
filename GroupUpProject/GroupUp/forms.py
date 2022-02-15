from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Group, Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')
    age = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError(
                "Can't create User and UserProfile without database save")
        user = super(SignUpForm, self).save(commit=True)
        user_profile = Profile(user=user, age=self.cleaned_data['age'])
        user_profile.save()
        return user, user_profile


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'owner', 'activity_name', 'activity_date',
                  'members', 'location', 'description')
        labels = {
            'name': '',
            'activity_name': 'Activity',
            'activity_date': 'YYYY-MM-DD HH:MM:SS',
            'members': 'Members',
            'location': 'Location',
            'description': 'Group Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Group Name'}),
            'activity_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Activity'}),
            'activity_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Activity Date'}),
            'members': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Members'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Trondheim'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }
