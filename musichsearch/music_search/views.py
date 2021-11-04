from django.shortcuts import render
from .utils import convert
from .forms import AudioForm

def home(request):
    return render(request, 'music_search/home.html')


# def music(request):
#     return render(request, 'music_search/music.html')

def Audio_store(request):
    form = AudioForm()
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            record = request.FILES['record']
            data = request.FILES['record'].name
            audio = record
            form.save()
            return render(request, 'music_search/demo.html', context={'data':data, 'audio':audio})
        else:
            form = AudioForm()
    return render(request, 'music_search/music.html', {'form' : form})

