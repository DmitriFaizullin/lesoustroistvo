from django.urls import path
from .views import *

urlpatterns = [
    path('', akt_constructor, name='akt_constructor'),
]
