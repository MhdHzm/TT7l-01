from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'settings.html') 
