from django.contrib import admin

# Register your models here.
from .models import Profile, Group, GroupReport


@admin.register(Profile, Group, GroupReport)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


"""
admin.site.register(Profile)
admin.site.register(Group)
"""