
from django.contrib import admin
from django.urls import path
from chatapp import views

urlpatterns = [
    path('', views.CreateRoom, name='create-room'),
    path('<str:room_name>/<str:username>/', views.MessageView, name='room'),
]
