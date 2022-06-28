"""tracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from .views import VehicleView, PathView, PathDetailView,PathVehicleView, VehicleTimeView, VehicleListView

router = DefaultRouter()
urlpatterns = [
                path('vehicle-detail/', VehicleView.as_view()),
                path('vehicle-detail/<int:id>/', VehicleView.as_view()),
                path('path/', PathView.as_view()),
                path('path/<int:id>/', PathView.as_view()),
                path('path-detail/', PathDetailView.as_view()),
                path('path-detail/<int:id>/', PathDetailView.as_view()),
                path('vehicle-path/', PathVehicleView.as_view()),
                path('vehicle-path/<int:id>/', PathVehicleView.as_view()),
                path('vehicle-time/', VehicleTimeView.as_view()),
                path('vehicle-list/', VehicleListView.as_view()),
] + router.urls