from django.shortcuts import render
from .models import RegisterUser
from .serializers import RegisterUserSerializer
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
import requests as rq
from rest_framework.parsers import JSONParser

class UserList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        user = RegisterUser.objects.filter(id=id)
        serializer = RegisterUserSerializer(user, many=True)
        get_user_detail = serializer.data
        if get_user_detail:
            response_data = {
                'success': True,
                'detail': get_user_detail
            }
            return Response(response_data, status=200)
        else:
            return Response({'success':False}, status=400)

    def post(self, request):
        data = JSONParser().parse(request)
        save_user_detail = RegisterUserSerializer(data=data)
        if save_user_detail.is_valid():
            save_user_detail.save()
            response_data = {
                    'success': True,
                    'msg': "your user detail saved successfully"
            }
            return Response(response_data, status=201)
        else:
            response_data = {
                    'success': False,
                    'msg': "your user detail not saved"
            }
            return Response(response_data, status=400)

    def delete(self, request, id,):
        user_del = RegisterUser.objects.filter(id=id).delete()
        if user_del:
            return Response({'success':True}, status=200)
        else:
            return Response({'success':False}, status=400)

    def put(self, request, id):
        user_update = RegisterUser.objects.get(id=id)
        serializer = RegisterUserSerializer(user_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                    'success': True,
                    'msg': "your user detail update successfully",
                    'result': serializer.data
            }
            return Response(response_data, status=200)
        else:
            response_data = {
                    'success': False,
                    'msg': "your user detail not update"
            }
            return Response(response_data, status=400)

    def patch(self, request, id):
        user_update = RegisterUser.objects.get(id=id)
        serializer = RegisterUserSerializer(user_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                    'success': True,
                    'msg': "your user detail update successfully",
                    'result': serializer.data
            }
            return Response(response_data, status=200)
        else:
            response_data = {
                    'success': False,
                    'msg': "your user detail not update"
            }
            return Response(response_data, status=400)