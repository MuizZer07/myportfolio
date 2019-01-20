from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^bio$', views.biopage, name='bio'),
    url(r'^music$', views.music, name='music'),
] 