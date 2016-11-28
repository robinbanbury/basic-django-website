from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact')
]

# 'views.index' is the 'index' function in the 'views.py' file. Due to our
# import statement, the 'views.py' file must be in this folder (and it is,
# a convention facilitated by Django).