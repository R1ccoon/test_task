
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('get/', views.GetAdsInfoView.as_view())
]
