from django.urls import path
from .views import wszystkie_filmy, nowy_film, edytuj_film


urlpatterns = [
    path('wszystkie/', wszystkie_filmy),    # jeśli url localhost/main/wszystkie to do funkcji wszystkie_filmy w views
    path('nowy/', nowy_film),
    path('edytuj/<int:id>/', edytuj_film)   # <int:id> pobiera numer id filmu który chcę edytować
]
