from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    chinesetitle = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    genres = models.CharField(max_length=200)
    director = models.CharField(max_length=100,default='')
    summary = models.TextField()
    fmt = models.CharField(max_length=20)
    length = models.PositiveIntegerField()
    rating = models.FloatField(default=1)
    url = models.URLField()
    img = models.URLField()

    def __unicode__(self):
        return self.title
