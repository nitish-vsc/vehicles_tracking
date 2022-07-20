from django.db import models
from users.models import RegisterUser

# Create your models here.

class Wallet(models.Model):
    user = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)
    amount = models.FloatField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class WalletHistory(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    debit_amount = models.FloatField(default=0)
    credit_amount = models.FloatField(default=0)
    updated_amount = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
