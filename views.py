from django.shortcuts import render
from django.http import HttpResponse

def receiver(request):
    return HttpResponse((input("Event name:")))