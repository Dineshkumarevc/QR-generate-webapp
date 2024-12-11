from django import forms
from .models import Payment
from .models import BankDetail
from django.contrib.auth.models import User

class SettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']  # Include any fields you want to be editable, e.g., phone number or profile fields



class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['phone_number', 'upi_number', 'amount']


class BankDetailForm(forms.ModelForm):
    class Meta:
        model = BankDetail
        fields = ['bank_name', 'account_number', 'ifsc_code']
        widgets = {
            'bank_name': forms.TextInput(attrs={'placeholder': 'Bank Name'}),
            'account_number': forms.TextInput(attrs={'placeholder': 'Account Number'}),
            'ifsc_code': forms.TextInput(attrs={'placeholder': 'IFSC Code'}),
        }
