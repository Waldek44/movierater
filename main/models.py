from django.db import models


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



# specjalna wbudowana funkcja str - za każdym razem kiedy używamy obiektu tej klasy, jest on reprezentowany przez nazwę (name) i rok (year)
    def __str__(self):
        return str(self.name) + " (" + str(self.year) + ")"
