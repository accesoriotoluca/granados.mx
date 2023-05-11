from django.urls import path
from .views import *

app_name = 'productos'

urlpatterns = [
    path('', productos, name='productos'),
]