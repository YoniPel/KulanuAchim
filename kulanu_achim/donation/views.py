from django.shortcuts import render
from .forms import ContactDonationForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.views.generic.edit import FormView

# Create your views here.

KA_EMAIL = settings.EMAIL_HOST_USER


def donation(request):
    return render(request, 'donation/donation.html')


class DonationItems(FormView):
    form_class = ContactDonationForm
    template_name = 'donation/donation_items.html'
    success_url = '/donation_success/'

    def form_valid(self, form):
        form.save()

        volunteer_name = form.cleaned_data.get('name_and_surname')
        volunteer_email = form.cleaned_data.get('email')
        volunteer_number = form.cleaned_data.get('phone_number')
        volunteer_item = form.cleaned_data.get('donated_item')

        subject = f'{volunteer_name} רוצה לתרום לכולנו אחים!'

        message = f' רוצה לתרום לכולנו אחים {volunteer_name}\n' \
                  f' כתובת המייל היא: {volunteer_email}\n' \
                  f' מספר הטלפון הוא: {volunteer_number}\n' \
                  f' הוא רוצה לתרום: {volunteer_item}'

        
        send_mail(subject, message, KA_EMAIL, [KA_EMAIL], fail_silently=False)
        messages.success(self.request, 'ההודעה נשלחה!')
        messages.success(self.request, 'ההודעה נשלחה!')
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, 'donation/donation.html', context={'form': form})


def donation_success(request):
    return render(request, 'donation/donation_success.html')


def donation_failure(request):
    return render(request, 'donation/donation_failure.html')
