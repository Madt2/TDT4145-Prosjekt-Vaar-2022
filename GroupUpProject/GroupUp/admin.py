from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    add_fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'age')}),
    )
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
