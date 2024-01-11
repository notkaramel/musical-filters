# Import Libraries
import os
os.environ['LIBROSA_CACHE_DIR'] = '/tmp/librosa_cache'
import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import IPython.display as ipd
import glob
import filters
import numpy as np
import soundfile as sf

if __name__ == "__main__":
    # Clear librosa cache
    librosa.cache.clear()

    audio_, sr_ = librosa.load('test_audios/beethoven5.mp3', mono=False, sr=None)
    print(np.shape(audio_)) #(2, 908460)
    print(audio_)

    #normalize audio
    #audio = filters.audio2img(audio_)

    audio = audio_

    #apply Gaussian blurring filter
    gauss = filters.gauss1D(25, 1)
    audio_filtered1 = filters.conv1D(audio[0], gauss)
    audio_filtered2 = filters.conv1D(audio[1], gauss)
    audio_filtered = np.array([audio_filtered1, audio_filtered2])
    print(audio_filtered)