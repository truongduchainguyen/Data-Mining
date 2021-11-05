import numpy as np
from pydub import AudioSegment
import subprocess
import pickle
import os
import librosa
import numpy as np

# import audio2numpy as a2n
def convert(audio_file):
    m4a_sound = AudioSegment.from_file(audio_file)
    result = m4a_sound.export("media/{0}.wav".format(audio_file.replace("D:/Google Drive/Data Mining/songs/", "").replace(".m4a", "")), 
                              format="wav")
    return result

# def convert(audio_file):
#     subprocess.call(['ffmpeg', '-i', audio_file,
#                  'converted_to_wav_file.wav'])


# def convert(audio_file):
#     x, sr = a2n.audio_from_file(audio_file)

def load_object():
    # file_to_read = open('musichsearch/Nazash_24_48_1000.pkl', "rb")
    file_to_read = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Nazash_24_48_1000.pkl'), 'rb')
    # print(type(file_to_read))
    loaded_object = pickle.load(file_to_read)
    file_to_read.close()
    return loaded_object

def hash_func(vecs, projections):
    bools = np.dot(vecs, projections.T) > 0
    return [bool2int(bool_vec) for bool_vec in bools]

def bool2int(x):
    y = 0
    for i,j in enumerate(x):
        if j: y += 1<<i
    return y

class Table:
    def __init__(self, hash_size, dim):
        self.table = dict()
        self.hash_size = hash_size
        self.projections =  np.random.randn(self.hash_size, dim)

    def add(self, vecs, label):
        entry = {'label': label}
        hashes = hash_func(vecs, self.projections)
        for h in hashes:
            if self.table.__contains__(h):
                self.table[h].append(entry)
            else:
                self.table[h] = [entry]

    def query(self, vecs):
        hashes = hash_func(vecs, self.projections)
        results = list()
        for h in hashes:
            if self.table.__contains__(h):
                results.extend(self.table[h])
        return results

class LSH:
    def __init__(self, dim):
        '''
        Nhận xét: Sau khi tăng num_tables và hash_size thì kết quả có cải thiện
        WHY?????
        '''
        self.num_tables = 6 # <----- Có thể improve được Tăng/giảm?
        self.hash_size = 24  # <----- Như trên
        self.tables = list()
        for i in range(self.num_tables):
            self.tables.append(Table(self.hash_size, dim))

    def add(self, vecs, label):
        for table in self.tables:
            table.add(vecs, label)

    def query(self, vecs):
        results = list()
        for table in self.tables:
            results.extend(table.query(vecs))
        return results

    def describe(self):
        for table in self.tables:
            print(table.table)

class MusicSearch:
    def __init__(self, training_files):
        self.frame_size = 4096 # 4096
        self.hop_size = 4000 # 4000
        self.fv_size = 12 #12
        self.lsh = LSH(self.fv_size)
        self.training_files = training_files
        self.num_features_in_file = dict()
        for f in self.training_files:
            self.num_features_in_file[f] = 0

    def train(self):
        # TODO: Sử dụng feature khác phù hợp hơn

        for filepath in self.training_files:
            x, fs = librosa.load(filepath)
            features = librosa.feature.chroma_stft(x, fs, n_fft=self.frame_size, hop_length=self.hop_size).T
            self.lsh.add(features, filepath)
            self.num_features_in_file[filepath] += len(features)

    def query_by_filepath(self, filepath):
        '''
        Hàm này query theo filepath:
        * Đọc audio file:
            - x: Audio time series
            - fs: sampling rate (mặc định: 22050 Hz)
        '''
        x, fs = librosa.load(filepath)
        # sliding windows
        features = librosa.feature.chroma_stft(x, fs, n_fft=self.frame_size, hop_length=self.hop_size).T
        results = self.lsh.query(features)
        print('num results '+ str(len(results)))

        counts = dict()
        for r in results:
            if counts.__contains__(r['label']):
                counts[r['label']] += 1
            else:
                counts[r['label']] = 1
        for k in counts:
            counts[k] = float(counts[k])/self.num_features_in_file[k]
        return counts

    def query(self, x, fs):
        features = librosa.feature.chroma_stft(x, fs, n_fft=self.frame_size, hop_length=self.hop_size).T
        results = self.lsh.query(features)
        print('num results '+ str(len(results)))

        counts = dict()
        for r in results:
            if counts.__contains__(r['label']):
                counts[r['label']] += 1
            else:
                counts[r['label']] = 1
        for k in counts:
            counts[k] = float(counts[k])/self.num_features_in_file[k]
        return counts
