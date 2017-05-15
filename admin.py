from pymovieshelf.models import Movie
from django.contrib import admin

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','chinesetitle','year')

admin.site.register(Movie,MovieAdmin)

