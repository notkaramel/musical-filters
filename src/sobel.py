import numpy as np
from IO import loadAudioFile, exportAudioFile
import cv2


def sobel_filter(audio):
    """Applies sobel filter on input audio, to detect... audio edges?

    Parameters:
    - audio (2D np.array): input audio
    - mode (int): 1 for copy audio left channel, 2 for right channel
    Returns: out_audio (2D np.array): filtered version of input audio

    Idea: since the audio is a 2xN signal, while the sobel filter is a 3x3 matrix, so...
    what if, we add a "3rd and 4th dimension" to the audio, and then apply the sobel filter?
    """
    # sobel filter
    sobel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    audio_left = audio[0]
    audio_right = audio[1]

    # create temporary 4xN array
    temp_4audio_left = np.array([audio_left, audio_right, audio_left])
    temp_4audio_right = np.array([audio_right, audio_left, audio_right])
    # print(temp_4audio.shape)

    # apply sobel filter
    out_audio = [[], []]
    out_audio[0] = cv2.filter2D(
        src=temp_4audio_left, ddepth=-1, kernel=sobel_x*100)
    out_audio[1] = cv2.filter2D(
        src=temp_4audio_right, ddepth=-1, kernel=sobel_y*100)
    return out_audio


if __name__ == "__main__":
    file = 'audio_files/beethoven5.mp3'
    # load audio file
    audio_arr, sr = loadAudioFile(file)

    # apply sobel filter
    out_audio = sobel_filter(audio_arr)

    # export audio
    exportAudioFile('audio_files/sobel_beethoven5.flac', audio_arr, sr)
