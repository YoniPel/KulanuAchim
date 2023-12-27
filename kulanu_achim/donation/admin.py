from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.ContactDonation)
class ContactHelpAdmin(admin.ModelAdmin):
    list_display = ('name_and_surname', 'address', 'email', 'phone_number', 'donated_item', 'created_at')