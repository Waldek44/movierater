from django.db import models


class ExtraInfo(models.Model):
    RODZAJE = {
        (0, 'Nieznany'),
        (1, 'Sci-fi'),
        (2, 'Komedia'),
        (3, 'Dramat'),
        (4, 'Akcja'),
        (5, 'Psychologiczny'),
    }
    czas_trwania = models.IntegerField(default=0)
    rodzaj = models.IntegerField(default=0, choices=RODZAJE)


# model filmów dodawanych do DB
class Movie(models.Model):
    name = models.CharField(max_length=122)
    description = models.TextField(default="")
    year = models.IntegerField(null=True, blank=True)
    relaesed = models.DateField(null=True, blank=True)
    # null - parametr (Field option) który określa, że pole nie jest wymagane
    # blank - podobnie jak null, dzięki niemu nie wywala w walidacji
    imdb_rating = models.DecimalField(null=True, blank=True, decimal_places=1, max_digits=2)
    photo = models.ImageField(null=True, blank=True, upload_to='filmowe')
    info = models.OneToOneField(
        ExtraInfo,
        on_delete=models.CASCADE,  # co się stanie z obiektem po usunięciu z bazy (CASCADE- też zostanie usunięty)
        primary_key=True,
    )


    # specjalna wbudowana funkcja str - za każdym razem kiedy używamy obiektu tej klasy,
    # jest on reprezentowany przez nazwę (name) i rok (year)
    def __str__(self):
        return str(self.name) + " (" + str(self.year) + ")"

class Review(models.Model):
    text = models.CharField(default='', blank=True, max_length=250)
    stars = models.IntegerField(default=3)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Aktor(models.Model):
    imie = models.CharField(max_length=55)
    nazwisko = models.CharField(max_length=55)
    movie = models.ManyToManyField(Movie)
