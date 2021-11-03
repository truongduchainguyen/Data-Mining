from django.shortcuts import render

def home(request):
    return render(request, 'music_search/home.html')


def music(request):
    return render(request, 'music_search/music.html')

def upload(request):
    form =
