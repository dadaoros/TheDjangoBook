from django.conf.urls import patterns, include, url

from mysite.views import hello, current_datetime


urlpatterns = patterns('',
    url(r'^hello/', hello),
    url(r'^time/$', current_datetime),
)





