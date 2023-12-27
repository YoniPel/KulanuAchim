from django.shortcuts import render


# Create your views here.


def activities(request):
    return render(request, 'activities/activities.html')


def purim_campaign(request):
    return render(request, 'activities/purimCampaign.html')


def passover_campaign(request):
    return render(request, 'activities/passoverCampaign.html')


def hanukkah_campaign(request):
    return render(request, 'activities/hanukkahCampaign.html')


def rosh_hashanah_campaign(request):
    return render(request, 'activities/roshHashanahCampaign.html')