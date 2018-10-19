from django.urls import path
from .views import wszystkie_filmy, nowy_film


urlpatterns = [
    path('wszystkie/', wszystkie_filmy),    # jeśli url localhost/main/wszystkie to do funkcji wszystkie_filmy w views
    path('nowy/', nowy_film)
]
