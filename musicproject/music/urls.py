from django.urls import path
from . import views


urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('info/<int:pk>', views.SongInfo.as_view()),
]