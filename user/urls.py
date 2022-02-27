from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SingupAPI),
    path('userInfo/', views.UserInfoAPI.as_view()),
    path('login/', views.LoginAPI),
    path('profile/<int:user_id>/', views.ProfileAPIView.as_view())
]
