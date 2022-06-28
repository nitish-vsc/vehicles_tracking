from django.shortcuts import render
from .models import WalletHistory, Wallet
from .serializers import WalletHistorySerializer, WalletSerializer
from rest_framework import serializers, status, filters, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
import requests as rq
from datetime import datetime, timedelta
from django.http import Http404

class WalletView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        user = Wallet.objects.filter(user_id=id)
        serializer = WalletSerializer(user, many=True)
        get_wallet = serializer.data
        if get_wallet:
            return Response({'success': True, 'detail': get_wallet}, status=200)
        else:
            return Response({'success':False}, status=400)

    def delete(self, request, id):
        wallet_del = Wallet.objects.filter(id=id).delete()
        if wallet_del:
            return Response({'success':True}, status=200)
        else:
            return Response({'success':False}, status=400)

    def patch(self, request, id):
        wallet_update = Wallet.objects.get(id=id)
        serializer = WalletSerializer(wallet_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                    'success': True,
                    'msg': "your wallet update successfully",
                    'result': serializer.data
            }
            return Response(response_data, status=200)
        else:
            return Response({'success': False, 'msg': "your walllet not update"}, status=400)

    def post(self, request):
        data = JSONParser().parse(request)
        save_wallet = WalletSerializer(data=data)
        if save_wallet.is_valid():
            save_wallet.save()
            return Response({'success': True, 'msg': "your wallet saved successfully"}, status=201)
        else:
            return Response({'success': False, 'msg': "your wallet not saved"}, status=400)

class WalletHistoryView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        user = WalletHistory.objects.filter(wallet_id=id)
        serializer = WalletHistorySerializer(user, many=True)
        wallet_history = serializer.data
        if wallet_history:
            return Response({'success': True, 'detail': wallet_history}, status=200)
        else:
            return Response({'success':False}, status=400)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            user = data['user']
            credit_amount = data['credit_amount']
            wallet = Wallet.objects.get(user_id=user)
            wallet_id = wallet.id
            amount = wallet.amount
            updated_amount = amount + credit_amount
            wallet_history = {'credit_amount':credit_amount, 'updated_amount': updated_amount, 'wallet': wallet_id}
            wallet_amount = {'id': wallet_id, 'amount': updated_amount, 'user': user}
            wallet_serializer = WalletSerializer(wallet, data=wallet_amount, partial=True)
            serializer = WalletHistorySerializer(data=wallet_history)
            if(serializer.is_valid() and wallet_serializer.is_valid()):
                serializer.save()
                wallet_serializer.save()
                return Response({'success': True, 'msg': "You amount add successfully"}, status=201)
            else:
                return Response({'success': False, 'msg': "You amount not add"}, status=400)
        except Exception as e:
            print(e)