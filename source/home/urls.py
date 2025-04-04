from django.urls import path
from . views import HomePageView, PrivacyPolicyPageView, TermsOfServicePageView


urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('privacy-policy/', PrivacyPolicyPageView.as_view(), name='privacy_policy'),
    path('terms-of-service/', TermsOfServicePageView.as_view(), name='terms_of_service'),
]
