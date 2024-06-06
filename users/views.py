from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return HttpResponse ("Welcome to Online Event Ticket Booking System!") 
