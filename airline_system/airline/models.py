from django.db import models

# Create your models here.

class Aircraft(models.Model):
    name = models.CharField(max_length=100)
    model_number = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.model_number})"

class Airport(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('Scheduled', 'Scheduled'),
        ('Delayed', 'Delayed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed')
    ])

    def __str__(self):
        return f"{self.flight_number} ({self.departure_airport.code} -> {self.arrival_airport.code})"

class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    ])

    def __str__(self):
        return f"Booking: {self.passenger} - {self.flight.flight_number} (Seat: {self.seat_number})"
