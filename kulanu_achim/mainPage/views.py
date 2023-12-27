from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactInfoForm, ContactHelpFirstPageForm, ContactHelpSecondPageForm
from .models import ContactHelp
from django.views.generic.edit import FormView
import os


def retrieve_urls(path):
    folder = os.path.join(settings.STATIC_ROOT, path)
    images_file_names = [file for file in os.listdir(folder)]
    images_urls = [os.path.join(settings.STATIC_URL, path, filename) for filename in images_file_names]
    return images_urls


# Create your views here.

def home(request):
    slideshow_path = r'assets/img/slideshows/homePageSlideshow'
    images_urls = retrieve_urls(slideshow_path)

    context = {
        'images_urls': images_urls
    }

    # render takes an HTML file from a specified path
    return render(request, 'mainPage/home.html', context=context)


def about(request):
    return render(request, 'mainPage/about.html')


def activities(request):
    return render(request, 'mainPage/activities.html')


def contact(request):
    return render(request, 'mainPage/contact.html')


def staff(request):
    return render(request, 'mainPage/staff.html')


KA_EMAIL = settings.EMAIL_HOST_USER


class Volunteer(FormView):
    form_class = ContactInfoForm
    template_name = 'mainPage/volunteer.html'
    success_url = '/volunteer/'

    def form_valid(self, form):
        form.save()

        # send the message to the email
        volunteer_name = form.cleaned_data.get('name')
        volunteer_email = form.cleaned_data.get('email')
        volunteer_number = form.cleaned_data.get('phone_number')
        volunteer_message = form.cleaned_data.get('message')

        subject = f'{volunteer_name} רוצה להתנדב בכולנו אחים!'

        message = f' רוצה להתנדב בכולנו אחים {volunteer_name}\n' \
                  f' כתובת המייל היא: {volunteer_email}\n' \
                  f' מספר הטלפון הוא: {volunteer_number}\n' \
                  f' הוא השאיר את ההודעה הבאה: {volunteer_message}'

        
        send_mail(subject, message, KA_EMAIL, [KA_EMAIL], fail_silently=False)
        messages.success(self.request, 'ההודעה נשלחה!')
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, 'mainPage/volunteer.html', context={'form': form})


class HelpFirstPage(FormView):
    form_class = ContactHelpFirstPageForm
    template_name = 'mainPage/helpFirstPage.html'

    def form_valid(self, form):
        instance = form.save()
        self.request.session['instance_id'] = instance.id
        return redirect('helpQuestionnairePage')

    def form_invalid(self, form):
        return render(self.request, 'mainPage/helpFirstPage.html', context={'form': form})


class HelpSecondPage(FormView):
    form_class = ContactHelpSecondPageForm
    template_name = 'mainPage/helpSecondPage.html'

    def form_valid(self, form):
        instance_id = self.request.session.get('instance_id')
        if instance_id:
            instance = ContactHelp.objects.get(id=instance_id)
            instance.health_status = form.cleaned_data['health_status']
            instance.rent_status = form.cleaned_data['rent_status']
            instance.vehicle_status = form.cleaned_data['vehicle_status']
            instance.work_status = form.cleaned_data['work_status']
            instance.income_status = form.cleaned_data['income_status']
            instance.debt_status = form.cleaned_data['debt_status']
            instance.classes_status = form.cleaned_data['classes_status']
            instance.clothes_status = form.cleaned_data['clothes_status']
            instance.furniture_status = form.cleaned_data['furniture_status']
            instance.air_conditioning_status = form.cleaned_data['air_conditioning_status']
            instance.appliances_and_kitchen_status = form.cleaned_data['appliances_and_kitchen_status']
            instance.cleaning_status = form.cleaned_data['cleaning_status']
            instance.notes = form.cleaned_data['notes']

            instance.save()

            names_and_surname = instance.names_and_surname
            address = instance.address
            number = instance.phone_number
            email = instance.email
            subject = f' משפחת {names_and_surname} זקוקה לסיוע '

            message = f' משפחת {names_and_surname} זקוקה לסיוע \n' \
                      f' כתובת המייל היא: {address}\n' \
                      f' מספר הטלפון הוא: {number}\n' \
                      f' הכתובת היא: {email}'

            
            send_mail(subject, message, KA_EMAIL, [KA_EMAIL], fail_silently=False)
            messages.success(self.request, 'ההודעה נשלחה!')

            self.request.session.pop('instance_id', None)
            return redirect('helpPage')

    def form_invalid(self, form):
        return render(self.request, 'mainPage/helpSecondPage.html', context={'form': form})


def fourth_wall(request):
    return render(request, 'mainPage/fourthWall.html')
