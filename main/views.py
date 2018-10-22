# from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm


def wszystkie_filmy(request):      # każda funkcja w views przyjmuje parametr request
    # return HttpResponse('testuję bo umiem')
    zmienna44 = "mięta" * 11
    zmienna_filmy = Movie.objects.all()
    return render(request, 'lista_filmow.html', {'filmowa': zmienna_filmy, 'text44': zmienna44})


def nowy_film(request):
    form = MovieForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form})


def edytuj_film(request, id):
    film = get_object_or_404(Movie, pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form})
