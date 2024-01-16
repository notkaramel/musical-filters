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

def loadAudioFile(filename) -> tuple:
    """
    Loads an audio file and returns a tuple of the audio array and the sampling rate.
    """
    audio, sr = librosa.load(filename, mono=False, sr=None)
    return audio, sr


def exportAudioFile(output_filename, audio_array, sampling_rate, file_format='flac'):
    """
    Exports an audio array into a file. By default, the file format is set to `flac`.
    """

    # Assuming you use loadAudioFile() to load the audio file, the audio_array
    # is a 2D numpy array with shape (2, number_of_samples).
    # To export using soundfile, the audio array needs to be transposed
    # so that the shape becomes (number_of_samples, 2).
    #
    # Documentation: https://python-soundfile.readthedocs.io/en/0.11.0/#soundfile.write
    audio_signal = np.matrix.transpose(audio_array)
    sf.write(output_filename, audio_signal, sampling_rate, format=file_format)

if __name__ == "__main__":

    file = 'audio_files/beethoven5.mp3'
    audio_arr, sr = loadAudioFile(file)

    print(np.shape(audio_arr)) #(2, 908460)
    print(audio_arr)

    #normalize audio
    #audio = filters.audio2img(audio_arr)

    #apply Gaussian blurring filter
    filter_size = 100
    sigma = 20
    gauss = filters.gauss1D(filter_size, sigma)
    audio_filtered1 = filters.conv1D(audio_arr[0], gauss)
    audio_filtered2 = filters.conv1D(audio_arr[1], gauss)
    audio_filtered = np.array([audio_filtered1, audio_filtered2])
    print(audio_filtered)
    
    exportAudioFile(f'audio_files/beethoven5_gauss_win{filter_size}_sig{sigma}.flac', audio_filtered, sr)
    