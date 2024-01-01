import librosa
import numpy as np

def waveshaping(audio_arr, function):
    audio_new = np.array(function(audio_arr))
    return audio_new

if __name__ == '__main__':
    y = lambda x: x**2 + 3*x + 1
    audio, sr = librosa.load('audio_samples/test.wav', mono=False, sr=None)
    new_audio = []
    for audio_channel in audio:
        new_audio.append(waveshaping(audio_channel, y))
    print(new_audio)
