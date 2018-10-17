# from django.http import HttpResponse
from django.shortcuts import render


def wszystkie_filmy(request):      # każda funkcja w views przyjmuje parametr request
    # return HttpResponse('testuję bo umiem')
    text11 = 'w ten sposób mogę przekazać zmienną pochodzącą z funkcji | wynik dodawania to: ' + str(44 + 11)
    zmienna_filmy = ['Avatar', '12 angry people', 'MadMax', 'MadMax2', 'MadMax3']
    return render(request, 'lista_filmow.html', {'text44': text11, 'filmowa': zmienna_filmy, 'moze_ogladac': True})

