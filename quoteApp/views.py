# quoteApp/views.py
from django.shortcuts import render
from django.http import HttpResponse

# สร้าง views ของคุณที่นี่
def displayQuote(request):
    return HttpResponse("The best investment we can make is in ourselves. - Warren Buffett")
