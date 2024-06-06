def home(request):
    message = "Welcome to Online Event Ticket Booking System!"
    return render(request, 'welcome.html',{'message': message})
