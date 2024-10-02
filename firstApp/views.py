# views.py
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def display(request):
    return HttpResponse("<h1>My First Django APP!</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Current Date & Time:</b> " + str(dt)
    return HttpResponse(s)

def displayQuote(request):
    return HttpResponse("<b>The best investment we can make is in ourselves. - Warren Buffett</b>")  # Update with your quote
