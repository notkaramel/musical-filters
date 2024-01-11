# Import Libraries
import os
os.environ['LIBROSA_CACHE_DIR'] = '/tmp/librosa_cache'
import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import IPython.display as ipd
import glob


if __name__ == "__main__":
    # Clear librosa cache
    librosa.cache.clear()

    audio_, sr_ = librosa.load('test_audios/beethoven5.mp3', mono=False, sr=None)
    print(audio_)