from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    year_prod = models.IntegerField()
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return self.title


class Theater(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=2, blank=True, default='')
    films = models.ManyToManyField(Film)

    class Meta:
        ordering = ('name',)
 