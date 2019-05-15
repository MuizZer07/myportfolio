from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^my_projects', views.my_projects, name='projects'),
    url(r'^project/(\d+)/', views.show_project, name='show_project'),
    url(r'^bin/', views.bin, name='bin'),
    url(r'^delete/text/(\d+)/', views.deletetext, name='deletetext'),
    url(r'^delete/file/(\d+)/', views.deletefile, name='deletefile'),
] 