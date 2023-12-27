from django.db import models


class ContactDonation(models.Model):
    name_and_surname = models.CharField(max_length=100, verbose_name='שם פרטי ושם משפחה')
    email = models.EmailField(verbose_name='מייל')
    phone_number = models.CharField(max_length=10, verbose_name='מספר טלפון')
    address = models.CharField(max_length=100, verbose_name='כתובת')
    donated_item = models.CharField(max_length=100, verbose_name='פריט')
    notes = models.TextField(max_length=500, verbose_name='פירוט', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='נשלח בתאריך')

    def __str__(self):
        return self.name_and_surname

    class Meta:
        verbose_name = 'תרומה של פריט'
        verbose_name_plural = 'תרומות של פריטים'
