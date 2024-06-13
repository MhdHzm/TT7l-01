from django.shortcuts import render

def home_screen_view(request):
    
    # context = {}
    # context['some_string'] = "this is some string that I'm passing to the view"
    # context['some_number'] = 141251

    context = {
        'some_string':"this is some string that I'm passing to the view",
        'some_number' : 124125,
    }
    
    return render(request, "project/home.html", {})
