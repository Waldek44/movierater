from django.forms import ModelForm
from .models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'year', 'relaesed', 'imdb_rating', 'photo']
        exclude = [] # w exclude mogę zawrzeć pola które chcę wykluczyć