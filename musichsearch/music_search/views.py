from django.shortcuts import render
# from .utils import load_object
from .forms import AudioForm
import librosa 
from .utils import *
import pickle
from django.core.files.storage import default_storage


def home(request):
    return render(request, 'music_search/home.html')


# def music(request):
#     return render(request, 'music_search/music.html')

def Audio_store(request):
    form = AudioForm()
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            audio = request.FILES['record']
            name = request.FILES['record'].name
            file_name = default_storage.save('songs/' + audio.name, audio)
            data = "media/songs/{}".format(name)
            my_nazash = load_object()
            # D:\Data-Mining\musichsearch\music_search\Nazash_24_48_1000.pkl
            test_sample, test_sr = librosa.load(data)
            
            results = my_nazash.query(test_sample, test_sr)
            sorted_song_by_results = sorted(results, key=results.get, reverse=True)
            searched_song = []
            idx = 0
            for r in sorted_song_by_results:
                searched_song.append("{}".format(r.replace("songs/train\\",'').replace(".m4a", '')))
                idx += 1
                if idx == 5:
                    break
            
            # link_song = convert("D:/Google Drive/Data Mining/songs/" + str(searched_song[0]) + ".m4a")
            link_song = str(searched_song[0])
            form.save()
            return render(request, 'music_search/demo.html', context={'searched_song':searched_song, 'audio':audio, 'link_song':link_song})
        else:
            form = AudioForm()
    return render(request, 'music_search/music.html', {'form' : form})

