from django.contrib import admin
from .models import Movie


# inna fajna forma rejestrowania modelu w panelu admina
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """ fields - pola które mają być wyświetlane na stronie edycji filmu
    fields = ('name', 'description') """

    list_display = ('name', 'year', 'imdb_rating', 'relaesed')
    list_filter = ('year', 'imdb_rating')   # filtr boczny
    search_fields = ('name', 'description')
    ordering = ('-imdb_rating', '-year')
