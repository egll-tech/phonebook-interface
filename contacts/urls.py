from django.urls import path
from django.contrib.admin import AdminSite

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]