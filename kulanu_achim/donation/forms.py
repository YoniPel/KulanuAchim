from django import forms
from . import models


class ContactDonationForm(forms.ModelForm):
    class Meta:
        model = models.ContactDonation
        fields = ['name_and_surname', 'address', 'phone_number', 'email', 'donated_item', 'notes']
