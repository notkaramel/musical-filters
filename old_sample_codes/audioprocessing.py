# Import Libraries
import os
os.environ['LIBROSA_CACHE_DIR'] = '/tmp/librosa_cache'
import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import IPython.display as ipd
import glob

# Clear librosa cache
librosa.cache.clear()

audio, sr = [], []
for file in glob.glob('audio_samples/*'):
    audio_, sr_ = librosa.load(file, mono=False, sr=None)
    audio.append(audio_)
    sr.append(sr_)

print(audio[1])
print(np.shape(audio[1]))
print(audio[1][0])

# Algorithm Concept
def remove_nth_index(arr, n):
    return [arr[i] for i in range(len(arr)) if (i + 1) % n != 0]

# Example usage:
input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3  # Replace 'n' with the desired index to remove

result = remove_nth_index(input_array, n)
print("Result:", result)

# Remove every nth sample of the audio file for compression
def remove_every_nth_sample(audio, sr:int, n:int):
    print(f'Removing every {n}-th sample')
    # Algorithm: keeping all samples that have index not divisible by n
    new_audio_left  = [audio[0][i] for i in range(len(audio[0])) if i % n != 0]
    new_audio_right = [audio[1][i] for i in range(len(audio[1])) if i % n != 0]

    # Append the two channels to a new array
    new_audio = np.array([new_audio_left, new_audio_right])

    # Compare the size of the original and new audio
    print(f'Original size: {round(audio.size/1e6)} MB 
          vs. New size: {round(new_audio.size/1e6)} MB')
    
    # New sampling rate = original sampling rate - number of samples removed
    # new_sr = sr - sr/n
    new_sr = sr*(1-1/n)
    return new_audio, new_sr


# Display audio file on Jupyter Notebook
ipd.Audio(audio[4], rate=sr[4])

# Compressed audio file by removing every 2nd sample
new_audio, new_audio_sr = remove_every_nth_sample(audio[4], sr[4], n=2)
ipd.Audio(new_audio, rate=new_audio_sr)

# Waveshaping
def waveshaping_poly(audio, sr, order=2):
    audio_poly = np.array([i**order for i in audio])
    ipd.display(ipd.Audio(audio_poly, rate=sr))


def waveshaping(audio, sr, function):
    audio_new = np.array(function(audio))
    ipd.display(ipd.Audio(audio_new, rate=sr))


def plot(function):
    plt.rcParams["figure.figsize"] = [4, 4]
    plt.rcParams["figure.autolayout"] = True
    x = np.linspace(-1, 1, 100)
    plt.plot(x, function(x), color='blue')

y = lambda x: abs(x)
plot(y)
waveshaping(audio[0], sr[0], y)