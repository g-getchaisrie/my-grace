#urls.py
from django.contrib import admin
from django.urls import path
from firstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.display),  # Add this line for the root URL
    path('hello/', views.display),
    path('datetime/', views.displayDateTime),
    path('quote/', views.displayQuote),
]
