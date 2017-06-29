from django.conf.urls import *
from pymovieshelf.views import MovieList,MovieDetailView
from django.views import generic

urlpatterns = patterns(
    '',
    (r'^$', 'pymovieshelf.views.index'),
    (r'^add_imdb/', 'pymovieshelf.views.add_imdb'),
    (r'^searchmovie/', 'pymovieshelf.views.searchmovie'),
    (r'^(?P<pk>\d+)/$',MovieDetailView.as_view()),
)
