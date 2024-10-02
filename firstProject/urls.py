# firstProject/urls.py
from django.contrib import admin
from django.urls import path
from firstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),               # เส้นทางสำหรับแผงผู้ดูแลระบบ
    path('', views.display),                       # เส้นทางสำหรับ root URL
    path('hello/', views.display),                 # เส้นทางสำหรับ hello
    path('datetime/', views.displayDateTime),      # เส้นทางสำหรับวันที่และเวลา
    path('quote/', views.displayQuote),            # เส้นทางสำหรับ quote
]
