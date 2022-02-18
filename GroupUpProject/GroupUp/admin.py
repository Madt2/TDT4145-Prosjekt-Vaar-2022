from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Group, Report, Interest


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
admin.site.register(Group)
admin.site.register(Report)
admin.site.register(Interest)
