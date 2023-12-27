from django.urls import path
from . import views

urlpatterns = [
    # path (path, what the user will see, name)
    path('', views.home, name='homePage'),
    path('about/', views.about, name='aboutPage'),
    path('contact/', views.contact, name='contactPage'),
    path('staff/', views.staff, name='staffPage'),
    path('volunteer/', views.Volunteer.as_view(), name='volunteerPage'),
    path('help/', views.HelpFirstPage.as_view(), name='helpPage'),
    path('help_questionnaire/', views.HelpSecondPage.as_view(), name='helpQuestionnairePage'),
    path('4/', views.fourth_wall, name='fourthWall'),
]
