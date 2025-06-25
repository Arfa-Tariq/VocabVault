from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # homepage
]

