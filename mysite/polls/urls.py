from django.urls import path
from . import views

from django.conf.urls import patterns, url
from app_name.views import *

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
)


urlpatterns = [
    path('', views.index, name='index'),
]
