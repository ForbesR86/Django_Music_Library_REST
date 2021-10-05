from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('', views.SongList.as_view()),
    path('music/<int:pk>/', views.SongDetails.as_view()),
    path('music/<int:pk>/<str:title>/', views.SongLike.as_view()),
]