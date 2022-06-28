from django.shortcuts import render
from .models import Vehicle, Path, PathDetail, VehiclePath
from .serializers import VehicleSerializer, PathSerializer, PathDetailSerializer, VehiclesPathSerializer
from wallet.serializers import WalletSerializer, WalletHistorySerializer
from wallet.models import WalletHistory, Wallet
from rest_framework import serializers, status, filters, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
import requests as rq
from datetime import datetime, timedelta
from django.http import Http404

class VehicleListView(generics.ListAPIView):
    search_fields = ['vehicle_type']
    filter_backends = (filters.SearchFilter,)
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        user = Vehicle.objects.filter(user_id=id)
        serializer = VehicleSerializer(user, many=True)
        get_vehicle_detail = serializer.data
        if get_vehicle_detail:
            return Response({'success': True, 'detail': get_vehicle_detail}, status=200)
        else:
            return Response({'success':False}, status=400)

    def post(self, request):
        data = JSONParser().parse(request)
        save_vehicle_detail = VehicleSerializer(data=data)
        if save_vehicle_detail.is_valid():
            save_vehicle_detail.save()
            return Response({'success': True, 'msg': "your vehicle detail saved successfully"}, status=201)
        else:
            return Response({'success': False, 'msg': "your vehicle detail not saved"}, status=400)

    def delete(self, request, id,):
        vehicle_del = Vehicle.objects.filter(id=id).delete()
        if vehicle_del:
            return Response({'success':True}, status=200)
        else:
            return Response({'success':False}, status=400)

    def put(self, request, id):
        vehicle_update = Vehicle.objects.get(id=id)
        serializer = VehicleSerializer(vehicle_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                    'success': True,
                    'msg': "your vehicle detail update successfully",
                    'result': serializer.data
            }
            return Response(response_data, status=200)
        else:
            return Response({'success': False, 'msg': "your vehicle detail not update"}, status=400)

    def patch(self, request, id):
        vehicle_update = Vehicle.objects.get(id=id)
        serializer = VehicleSerializer(vehicle_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                    'success': True,
                    'msg': "your vehicle detail update successfully",
                    'result': serializer.data
            }
            return Response(response_data, status=200)
        else:
            return Response({'success': False, 'msg': "your vehicle detail not update"}, status=400)

class PathView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        path = Path.objects.filter(user_id=id)
        serializer = PathSerializer(path, many=True)
        if serializer:
            return Response({'success': True, 'detail': serializer.data}, status=200)
        else:
            return Response({'success':False}, status=400)

    def post(self, request):
        data = JSONParser().parse(request)
        save_path_detail = PathSerializer(data=data)
        if save_path_detail.is_valid():
            save_path_detail.save()
            return Response({'success': True, 'msg': "your path saved successfully"}, status=201)
        else:
            return Response({'success': False, 'msg': "your path not saved"}, status=400)

    def delete(self, request, id,):
        path_del = Path.objects.filter(id=id).delete()
        if path_del:
            return Response({'success':True}, status=200)
        else:
            return Response({'success':False}, status=400)

    def put(self, request, id):
        path_update = Path.objects.get(id=id)
        serializer = PathSerializer(path_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'msg': "your path update successfully", 'result': serializer.data}, status=200)
        else:
            return Response({'success': False, 'msg': "your path not update"}, status=400)

    def patch(self, request, id):
        path_update = Path.objects.get(id=id)
        serializer = PathSerializer(path_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'msg': "your path update successfully", 'result': serializer.data}, status=200)
        else:
            return Response({'success': False, 'msg': "your path not update"}, status=400)

class PathDetailView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        path_detail = PathDetail.objects.filter(path_id=id)
        serializer = PathDetailSerializer(path_detail, many=True)
        if serializer:
            return Response({'success': True, 'detail': serializer.data}, status=200)
        else:
            return Response({'success':False}, status=400)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            for x in data:
                path_detail = PathDetailSerializer(data=x)
                if path_detail.is_valid():
                    path_detail.save()
            return Response({'success': True, 'msg': "your path detailt saved"}, status=200)
        except data.DoesNotExist:
            raise Http404
        else:
            return Response({'success': False, 'msg': "your path detailt not saved"}, status=400)

    def delete(self, request, id,):
        path_detail_del = PathDetail.objects.filter(id=id).delete()
        if path_detail_del:
            return Response({'success':True}, status=200)
        else:
            return Response({'success':False}, status=400)

    def put(self, request, id):
        path_detail_update = PathDetail.objects.get(id=id)
        serializer = PathDetailSerializer(path_detail_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                    'success': True,
                    'msg': "your path detail update successfully",
                    'result': serializer.data
            }
            return Response(response_data, status=200)
        else:
            return Response({'success': False, 'msg': "your path detail not update"}, status=400)

    def patch(self, request, id):
        path_detail_update = PathDetail.objects.get(id=id)
        serializer = PathDetailSerializer(path_detail_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                    'success': True,
                    'msg': "your path detail update successfully",
                    'result': serializer.data
            }
            return Response(response_data, status=200)
        else:
            return Response({'success': False, 'msg': "your path detail not update"}, status=400)

class VehicleTimeView(APIView):
    permission_classes = (AllowAny,)
    def patch(self, request):
        try:
            path_detail = PathDetail.objects.filter(path_id=request.data['path'])
            path_detail_obj = PathDetail.objects.get(id=request.data['detail_id'])
            dto = datetime.strptime(request.data['arrival_time'], '%Y-%m-%d %H:%M:%S')
            for route in path_detail:
                if route.distance == path_detail_obj.distance:
                    time_dict = {'id': route.id, 'arrival_time': dto}
                elif route.distance > path_detail_obj.distance:
                    current_distance = route.distance - path_detail_obj.distance
                    time = current_distance/30
                    time = time*60
                    dtuo = dto + timedelta(hours=0, minutes=time)
                    print(dtuo)
                    time_dict = {'id': route.id, 'arrival_time': dtuo}
                else:
                    current_distance = path_detail_obj.distance - route.distance
                    time = current_distance/30
                    time = time*60
                    dtuo = dto - timedelta(hours=0, minutes=time)
                    print(dtuo)
                    time_dict = {'id': route.id, 'arrival_time': dtuo}
                serializer = PathDetailSerializer(route, data=time_dict, partial=True)
                if serializer.is_valid():
                    serializer.save()
            return Response({'success': True, 'msg': "your current path time update"}, status=200)
        except PathDetail.DoesNotExist:
            raise Http404
        else:
            return Response({'success': False, 'msg': "your current path time not update"}, status=400)

class PathVehicleView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        vehicle_path = VehiclePath.objects.filter(id=id)
        serializer = VehiclesPathSerializer(vehicle_path, many=True)
        if serializer:
            return Response({'success': True, 'detail': serializer.data}, status=200)
        else:
            return Response({'success':False}, status=400)

    def post(self, request, id):
        try:
            data = JSONParser().parse(request)
            save_vehicle_path = VehiclesPathSerializer(data=data)
            path = Path.objects.get(id=id)
            user = data['user']
            wallet = Wallet.objects.get(user_id=user)
            wallet_id = wallet.id
            price = 5   # per kilometer
            debit_amount = price * path.distance
            updated_amount = wallet.amount - debit_amount
            # credit_amount = 0
            wallet_history = {'debit_amount':debit_amount, 'updated_amount': updated_amount, 'wallet': wallet_id}
            wallet_amount = {'id': wallet_id, 'amount': updated_amount, 'user': user}
            wallet_serializer = WalletSerializer(wallet, data=wallet_amount, partial=True)
            serializer = WalletHistorySerializer(data=wallet_history)
            if(save_vehicle_path.is_valid() and serializer.is_valid() and wallet_serializer.is_valid()):
                serializer.save()
                save_vehicle_path.save()
                wallet_serializer.save()
                return Response({'success': True, 'msg': "vehicle path saved successfully"}, status=201)
            else:
                return Response({'success': False, 'msg': "vehicle path not saved"}, status=400)
        except Exception as e:
            print(e)

    def delete(self, request, id,):
        vehicle_path_del = VehiclePath.objects.filter(id=id).delete()
        if vehicle_path_del:
            return Response({'success':True}, status=200)
        else:
            return Response({'success':False}, status=400)

    def put(self, request, id):
        vehicle_path_update = VehiclePath.objects.get(id=id)
        serializer = VehiclesPathSerializer(vehicle_path_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                    'success': True,
                    'msg': "your path detail update successfully",
                    'result': serializer.data
            }
            return Response(response_data, status=200)
        else:
            return Response({'success': False, 'msg': "your path detail not update"}, status=400)

    def patch(self, request, id):
        vehicle_path_update = VehiclePath.objects.get(id=id)
        serializer = VehiclesPathSerializer(vehicle_path_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                    'success': True,
                    'msg': "your path detail update successfully",
                    'result': serializer.data
            }
            return Response(response_data, status=200)
        else:
            return Response({'success': False, 'msg': "your path detail not update"}, status=400)