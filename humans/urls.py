from django.conf.urls.defaults import *

from humans import views

urlpatterns = patterns('',
    url(r'$', views.humans, name='humans'),
)
