from django.urls import path
from . import views

urlpatterns = [
    path('json', views.autocompleteJSON, name='json'),
    path('example', views.example)
]