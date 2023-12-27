from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.ContactInfo)
class ContactHelpAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'role', 'message', 'created_at')


@admin.register(models.ContactHelp)
class ContactHelpAdmin(admin.ModelAdmin):
    list_display = ('names_and_surname', 'address', 'email', 'phone_number', 'created_at')

@admin.register(models.Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'role', 'message')
