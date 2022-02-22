from django.conf.urls import url
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [

    path('post/',
         csrf_exempt(views.InstagramPostUpload.as_view()),
         name='instagram-upload'),

    path('post/list/',
         views.InstagramPostList.as_view(),
         name='instagram-list'),

    path('post/list/all/',
         views.InstagramPostAll.as_view(),
         name='instagram-list-all')
]
