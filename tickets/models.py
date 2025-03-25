from django.db import models
from movies.models import Movie
from django.conf import settings

class SeatType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price_multiplier = models.DecimalField(max_digits=3, decimal_places=2, default=1.0)
    
    def __str__(self):
        return self.name

class Ticket(models.Model):
    TICKET_TYPES = [
        ('ADULT', 'Người lớn'),
        ('CHILD', 'Trẻ em'),
    ]
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=5, choices=TICKET_TYPES)
    showtime = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_type = models.ForeignKey(SeatType, on_delete=models.SET_NULL, null=True, blank=True)
    seat_number = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.movie.title} - {self.showtime}"
    
    def get_final_price(self):
        if self.seat_type:
            return self.price * self.seat_type.price_multiplier
        return self.price

class TicketHolder(models.Model):
    HOLDER_TYPES = [
        ('ADULT', 'Người lớn'),
        ('CHILD', 'Trẻ em'),
    ]
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=5, choices=HOLDER_TYPES)
    age = models.IntegerField()
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
