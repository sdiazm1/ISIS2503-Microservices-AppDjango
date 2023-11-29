from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^places/', views.PlaceList),
    url(r'^placescreate/$', csrf_exempt(views.PlaceCreate), name='placeCreate'),
    url(r'^createplaces/$', csrf_exempt(views.PlacesCreate), name='createPlaces'),
]