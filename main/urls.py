from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView, name='home'),
    path('room/<str:pk>/', RoomView, name='room'),
    path('create-room/', CreateRoomView, name='create-room'),
    path('update-room/<str:pk>', UpdateRoomView, name='update-room'),
    path('delete-room/<str:pk>', DeleteRoomView, name='delete-room')
]