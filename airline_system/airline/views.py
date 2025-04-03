from django.shortcuts import render
from .models import Flight

# Create your views here.

def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'airline/flight_list.html', {'flights': flights})

from django.shortcuts import redirect
from .models import Booking, Passenger

def book_flight(request, flight_id):
    passenger = Passenger.objects.get(id=1)  # Replace with actual passenger login logic
    flight = Flight.objects.get(id=flight_id)
    Booking.objects.create(passenger=passenger, flight=flight, seat_number="A1", status="Confirmed")
    return redirect('flight_list')
