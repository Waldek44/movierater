from django.urls import path
from .views import wszystkie_filmy, nowy_film, edytuj_film, usun_film
"""
do path dodaję atrybut 'name' aby potem w templatkach
móc się do nich odwoływać, przykład: {% url 'name' film.id %}
-------------------------------
<int:id> pobiera numer id filmu który chcę edytować
"""

urlpatterns = [
    path('wszystkie/', wszystkie_filmy, name='wszystkie_filmy'),     # jeśli url localhost/main/wszystkie to do funkcji wszystkie_filmy w views
    path('nowy/', nowy_film, name='nowy_film'),
    path('edytuj/<int:id>/', edytuj_film, name='edytuj_film'),
    path('usun/<int:id>/', usun_film, name='usun_film')
]
