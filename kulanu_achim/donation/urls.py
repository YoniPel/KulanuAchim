from django.urls import path
from .views import donation, DonationItems, donation_success, donation_failure

urlpatterns = [
    # path (path, what the user will see, name)
    path('donation/', donation, name='donationPage'),
    path('donation/items', DonationItems.as_view(), name='donationItemsPage'),
    path('donation_success/', donation_success, name='donationSuccessPage'),
    path('donation_failure/', donation_failure, name='donationFailurePage')
]
