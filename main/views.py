from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q


# from django


def HomeView(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = RoomModel.objects.filter(Q(topic__name__icontains=q) |
                                     Q(name__icontains=q))
    topics = TopicModel.objects.all()
    return render(request, 'pages/home.html', context={
        'rooms': rooms,
        'topics': topics
    })


def RoomView(request, pk):
    room = RoomModel.objects.get(id=pk)
    return render(request, 'pages/room.html', context={
        'room': room
    })


def CreateRoomView(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'pages/room_form.html', context={
        'form': form
    })


def UpdateRoomView(request, pk):
    room = RoomModel.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'pages/room_form.html', context={
        'form': form
    })


def DeleteRoomView(request, pk):
    room = RoomModel.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'pages/delete.html', context={
        'obj': room
    })
