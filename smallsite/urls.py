from django.urls import path

from . import views

app_name = 'smallsite'
urlpatterns = [
    path('', views.index, name='index'),
    path('object/', views.launch_object_search, name='objectresult'),
]
