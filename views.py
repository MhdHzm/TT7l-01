from django.shortcuts import render
from .models import MyModel

def my_view(request):
    objects = MyModel.objects.all() 
    return render(request, 'myapp/my_template.html', {'objects': objects})
