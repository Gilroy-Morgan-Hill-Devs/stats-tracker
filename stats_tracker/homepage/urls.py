from django.conf.urls import patterns, url

from stats_tracker.homepage.views import Homepage

urlpatterns = patterns(
    '',
    url(r'^$', Homepage.as_view()),
)
