from  django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Flight,Passenger
# Create your views here.
def index(request):
    return render(request,"flights/index.html",{
        "flights":Flight.objects.all()
    })
def flight(request,flight_id):
    diff_flight = Flight.objects.get(id = flight_id)
    return render(request,"flights/flight.html",{
        "flight":diff_flight,
        "passengers":diff_flight.passengers.all(),
        "non_passengers":Passenger.objects.exclude(passenger_flights = diff_flight).all()
    })
def book(request,flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(id = flight_id)
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
        passenger.passenger_flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args = (flight_id,)))