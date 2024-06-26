from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# import the models
from .models import *


# Register your models here.
admin.site.register(Medicament)
admin.site.register(Agent)
admin.site.register(Achat)
admin.site.register(Profile)

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"
    # Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]
    # Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)