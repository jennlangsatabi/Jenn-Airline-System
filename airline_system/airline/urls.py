from django.urls import path
from . import views

urlpatterns = [
    path('flights/', views.flight_list, name='flight_list'),
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
]
