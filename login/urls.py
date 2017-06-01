from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from .views import login_view, logout_view, register_view

urlpatterns = [
    url(r'^login', login_view, name='login'),
    url(r'^logout', logout_view, name='logout'),
    url(r'^register', register_view, name='register'),
]