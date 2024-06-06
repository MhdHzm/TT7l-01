from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
  event_type = models.CharField(max_length=200)
  venue = models.TextField()
  date = models.DateField()
  time = models.TimeField()
  location = models.CharField(max_length=200)

  def __str__(self):
      return self.title

class Registration (models.Model):
  user = models.ForeignKey(Event, on_delete=models.CASCADE)
  event = models.ForeignKey(Online, on_delete=models.CASCADE)
  registration_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user.username} - {self.event.title}"

class Ticket(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  ticket_type = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  quantity = models.IntegerField()

  def __str__(self):
    return f"{self.event.title} - {self.ticket_type} Ticket"
