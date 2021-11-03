from django.http.response import HttpResponse
from django.shortcuts import render

from .forms import AudioForm

def home(request):
    return render(request, 'music_search/home.html')


# def music(request):
#     return render(request, 'music_search/music.html')

def Audio_store(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponse('sucessfully uploaded')
    else:
        form = AudioForm
    return render(request, 'music_search/music.html', {'form' : form})
