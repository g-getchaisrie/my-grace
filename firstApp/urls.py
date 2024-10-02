# firstApp/urls.py
from django.urls import path
from firstApp.views import display, displayDateTime

urlpatterns = [
    path('hello/', display, name='hello'),  # เส้นทางสำหรับ hello
    path('datetime/', displayDateTime, name='datetime'),  # เส้นทางสำหรับวันที่และเวลา
]

