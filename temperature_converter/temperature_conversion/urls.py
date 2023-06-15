from django.urls import path
from .views import temperature_converter_soap_service

urlpatterns = [
    path('converter/', temperature_converter_soap_service),
]
