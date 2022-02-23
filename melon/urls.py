from django.urls import path

from melon.views import MelonView

urlpatterns = [
    path('list/', MelonView.as_view()),
]
