from django.shortcuts import render, redirect, get_object_or_404
from .forms import PaymentForm, BankDetailForm  # Import both forms together
from .models import Payment, BankDetail  # Import both models together
import qrcode
from io import BytesIO
from django.core.files import File
# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import BankDetail  # Assuming you have a BankDetail model
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SettingsForm

@login_required
def settings(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your settings have been updated!')
            return redirect('settings')  # Redirect back to the settings page to show updated data
    else:
        form = SettingsForm(instance=request.user)

    return render(request, 'settings.html', {'form': form})






# Welcome Page View
def welcome_page(request):
    return render(request, 'gpay_app/welcome.html')


# Create Payment and Generate QR Code View
def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            # Generate QR code for payment
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr_data = f"upi://pay?pa={payment.upi_number}&pn={payment.phone_number}&am={payment.amount}"
            qr.add_data(qr_data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            buffer = BytesIO()
            img.save(buffer)
            filename = f'qr_{payment.phone_number}.png'
            payment.qr_code.save(filename, File(buffer), save=False)
            payment.save()

            return redirect('display_qr', pk=payment.pk)
    else:
        form = PaymentForm()
    return render(request, 'gpay_app/create_payment.html', {'form': form})


# Display QR Code View
def display_qr(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'gpay_app/display_qr.html', {'payment': payment})

def help(request):
    return render(request, 'help.html')

def contact(request):
    return render(request, 'gpay_app/contact.html')

def settings(request):
    return render(request, 'gpay_app/settings.html')

def link(request):
    return render(request, 'gpay_app/link.html')

def text(request):
    return render(request, 'gpay_app/text.html')

def image(request):
    return render(request, 'gpay_app/image.html')

def footer(request):
    return render(request, 'gpay_app/footer.html')


def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def qr_scanner(request):
    return render(request, 'gpay_app/scanner.html')

