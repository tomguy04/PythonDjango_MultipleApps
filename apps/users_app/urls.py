from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^users/$', views.users),
    url(r'^login/$', views.login),     # This line has changed!
    url(r'^register/$', views.register)     # This line has changed!
]


#url(r'^drinks/(?P<drink_name>\D+)/'

#
  
