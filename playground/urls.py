import imp
from django.urls import path
from . import views

#URL conf
urlpatterns = [
    path('home/', views.welcome),
    path('about/', views.about),
    path('contact/', views.contact)
]
