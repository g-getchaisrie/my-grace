# quoteApp/urls.py
from django.urls import path
from .views import displayQuote

urlpatterns = [
    path('quote/', displayQuote, name='displayQuote'),
]
