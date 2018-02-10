from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    # url(r'^(?P<number>\d+)/delete/$', views.destroy),
    # url(r'^(?P<number>\d+)/edit/$', views.edit),
    # url(r'^(?P<number>\d+)/$', views.show),
    # url(r'^create/$', views.create),
    url(r'^surveys/new/$', views.surveys_new),  
    url(r'^surveys/$', views.surveys)     # This line has changed!
]


#url(r'^drinks/(?P<drink_name>\D+)/'

#
  
