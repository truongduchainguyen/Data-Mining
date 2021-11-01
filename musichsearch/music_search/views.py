from django.shortcuts import render

def home(request):
    return render(request, 'music_search/home.html')
