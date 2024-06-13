from django.contrib import admin
from django.urls import path

from project.views import (
    home_screen_view,
    home_screen_view
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view),
]
