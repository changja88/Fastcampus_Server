from django.urls import path

from json_test.views import JsonTestView

urlpatterns = [
    path('students/', JsonTestView.as_view()),
]
