from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome'),  # Home page
    path('create/', views.create_payment, name='create_payment'),  # Create payment page
    path('qr/<int:pk>/', views.display_qr, name='display_qr'),  # Display QR code page
    
    path('help/', views.help, name='help'),  # Help page
    path('contact/', views.contact, name='contact'),
    path('settings/', views.settings, name='settings'),  # Settings page
    path('link/', views.link, name='link'), 
    path('text/', views.text, name='text'),
    path('image/', views.image, name='image'),  
    path('footer/', views.footer, name='footer'),  
    path('terms/', views.terms_of_service, name='terms_of_service'),
    path('privacy-policy.html', views.privacy_policy, name='privacy_policy'),
     path('qr-scanner/', views.qr_scanner, name='qr_scanner'),
]
   