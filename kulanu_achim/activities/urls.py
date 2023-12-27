from django.urls import path
from . import views

urlpatterns = [
    # path (path, what the user will see, name)
    path('activities/', views.activities, name='activitiesPage'),
    path('activities/purim_campaign', views.purim_campaign, name='purimCampaignPage'),
    path('activities/passover_campaign', views.passover_campaign, name='passoverCampaignPage'),
    path('activities/hanukkah_campaign', views.hanukkah_campaign, name='hanukkahCampaignPage'),
    path('activities/rosh_hashanah_campaign', views.rosh_hashanah_campaign, name='roshHashanahCampaignPage')

]
