import librosa
import soundfile as sf
import numpy as np


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


if __name__ == '__main__':
    # you can change this to any audio file you want
    file = 'audio_files/Im-lost-in-space-jan6.wav'
    audio_arr, sr = loadAudioFile(file)
    export2wav('test_export.flac', audio_arr, sr)
