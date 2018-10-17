from django.urls import path
from .views import wszystkie_filmy


urlpatterns = [
    path('wszystkie/', wszystkie_filmy)    # jeśli url localhost/main/wszystkie to do funkcji wszystkie_filmy w views
]
