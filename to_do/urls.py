from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToDoView.as_view()),
    path('search/', views.ToDoSearchView.as_view()),
]
