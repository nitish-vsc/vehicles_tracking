from rest_framework import serializers
from .models import Wallet, WalletHistory

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'amount', 'user']

class WalletHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletHistory
        fields = ['updated_amount', 'debit_amount', 'credit_amount', 'wallet']