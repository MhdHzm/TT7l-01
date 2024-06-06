from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('myadmin/', admin.site.urls),
    path('myaccounts/', include('allauth.urls')), 
    path('', include('users.urls',namespace='users')),  
]
