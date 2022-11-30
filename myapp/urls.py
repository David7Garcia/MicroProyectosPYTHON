from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('hello/<str:username>', views.hello),
    path('about/', views.about),
    path('projects/', views.projects),
    path('task/<str:tittle>', views.task)
]