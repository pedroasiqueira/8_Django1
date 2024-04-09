# playlists/views.py

from django.shortcuts import render, redirect
from playlists.forms import CreateMusicModelForm, CreateSingerForm
from playlists.models import Music, Singer


def music(request):
    # print('POSTTTT', request.POST)
    # print('BODYYYY', request.body)
    # print('METHODDDD', request.method)
    form = CreateMusicModelForm()
    if request.method == "POST":
        form = CreateMusicModelForm(request.POST)

        if form.is_valid():
            Music.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "music.html", context)


def singer(request):
    sing = CreateSingerForm()
    if request.method == "POST":
        sing = CreateSingerForm(request.POST)

        if sing.is_valid():
            Singer.objects.create(**sing.cleaned_data)
            return redirect("home-page")

    context = {"sing": sing}

    return render(request, "sing.html", context)


def index(request):
    context = {"musics": Music.objects.all()}
    return render(request, "home.html", context)
