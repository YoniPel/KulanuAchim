from django import forms
from . import models


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = models.ContactInfo
        fields = ['name', 'email', 'phone_number', 'role', 'message']


class ContactHelpFirstPageForm(forms.ModelForm):
    class Meta:
        model = models.ContactHelp
        fields = ['names_and_surname', 'address', 'phone_number', 'email', 'number_of_persons']
        widgets = {
            'number_of_persons': forms.Textarea(attrs={'rows': 4}),
        }


class ContactHelpSecondPageForm(forms.ModelForm):
    class Meta:
        model = models.ContactHelp
        fields = ['health_status', 'rent_status', 'vehicle_status', 'work_status', 'income_status',
                  'debt_status', 'classes_status', 'baby_status', 'clothes_status', 'furniture_status',
                  'air_conditioning_status', 'appliances_and_kitchen_status', 'cleaning_status',
                  'notes']

    def __init__(self, *args, **kwargs):
        super(ContactHelpSecondPageForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({'rows': 4})


