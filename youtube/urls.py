from django.urls import path

from youtube.views import YoutubeView

urlpatterns = [
    path('list/', YoutubeView.as_view()),
]
