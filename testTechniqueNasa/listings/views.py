from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
                        <h1>Hello Django!</h1>
                        <p>Mes groupes préférés sont : <p>
                        <li>{bands[0].name}</li>
                        <li>{bands[1].name}</li>
                        <li>{bands[2].name}</li>
                        <li>{bands[3].name}</li>
                        </p>
                        """)


def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous aimons NasaTest</p>')


def listings(request):
    return HttpResponse('<h1>Annonces</h1> <p>Nouvelle annonce pour les articles</p>')


def contact(request):
    return HttpResponse('<h1>Contact us</h1> <p>Nous contacter</p>')
