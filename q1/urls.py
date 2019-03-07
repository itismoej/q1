from django.contrib import admin
from django.urls import path
from req import views


urlpatterns = [
    path('req', views.req),
]
