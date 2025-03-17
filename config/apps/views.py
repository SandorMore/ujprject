from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Place
# Create your views here.
def GetPlace(self):
    places = Place.objects.all()
    placesList = []
    for place in places:
        placesList.append({
            'id': place.id,
            'name': place.name,
            'available': place.available,
        })