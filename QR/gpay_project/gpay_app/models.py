from django.db import models
# models.py
from django.db import models

class BankDetail(models.Model):
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"



class Payment(models.Model):
    phone_number = models.CharField(max_length=15)
    upi_number = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True)

    def _str_(self):
        return f"Payment - {self.phone_number}"
   
class BankDetail(models.Model):
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"


