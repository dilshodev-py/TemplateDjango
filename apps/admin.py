from django.contrib.admin import ModelAdmin , register , site
from django.contrib.auth.models import User, Group

from apps.models import Employee

site.unregister(User)
site.unregister(Group)

@register(Employee)
class EmployeeAdmin(ModelAdmin):
    pass
