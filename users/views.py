from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return HttpResponse ("Welcome to Online Event Ticket Booking System!")

def profile(request):
    return render(request, 'profile.html') 
