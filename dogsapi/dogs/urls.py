
"""
Book: Building RESTful Python Web Services
"""
# Remember to import the appropriate class  
# Incase you receive an error here because of the Djnago version you have installed

# from django.urls import re_path -  Use this incase
from django.urls import re_path
from dogs import views


urlpatterns = [
    re_path(r'^dogs/$', views.DogList.as_view(), name=views.DogList.name),
    re_path(r'^dogs/(?P<pk>[0-9]+)/$', views.DogDetail.as_view(), name=views.DogDetail.name),
    re_path(r'^breeds/$', views.BreedList.as_view(), name=views.BreedList.name),
    re_path(r'^breeds/(?P<pk>[0-9]+)/$', views.BreedDetail.as_view(), name=views.BreedDetail.name),
    re_path(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name)
]
