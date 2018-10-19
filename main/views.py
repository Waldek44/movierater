# from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


def wszystkie_filmy(request):      # każda funkcja w views przyjmuje parametr request
    # return HttpResponse('testuję bo umiem')
    zmienna44 = "mięta" * 11
    zmienna_filmy = Movie.objects.all()
    return render(request, 'lista_filmow.html', {'filmowa': zmienna_filmy, 'text44': zmienna44})
