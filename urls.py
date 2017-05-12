from django.conf.urls import *
from pymovieshelf.views import MovieList,MovieDetailView
from django.views import generic

urlpatterns = patterns(
    '',
    (r'^$', MovieList.as_view()),
    (r'^add_imdb/', 'pymovieshelf.views.add_imdb'),
    (r'^search/', 'pymovieshelf.views.search'),
    (r'^(?P<pk>\d+)/$',MovieDetailView.as_view()),
)
