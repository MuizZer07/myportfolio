from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^my_projects', views.my_projects, name='projects'),
    url(r'^project/(\d+)/', views.show_project, name='show_project'),
    url(r'^bin/', views.bin, name='bin'),
    url(r'^delete/text/(\d+)/', views.deletetext, name='deletetext'),
    url(r'^delete/file/(\d+)/', views.deletefile, name='deletefile'),
    url(r'^text/new/', views.savetext, name='savetext'),
    url(r'^file/new/', views.savefile, name='savefile'),
    url(r'^my_top_10s', views.my_top_10s, name='top_10s'),
    url(r'^my_ratings', views.my_ratings, name='my_ratings'),
] 