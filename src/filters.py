# Import Libraries
import os
os.environ['LIBROSA_CACHE_DIR'] = '/tmp/librosa_cache'
import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import glob
import cv2 as cv

'''
# Clear librosa cache
librosa.cache.clear()

audio, sr = [], []
for file in glob.glob('audio_samples/*'):
    audio_, sr_ = librosa.load(file, mono=False, sr=None)
    audio.append(audio_)
    sr.append(sr_)
'''


#manual convolution
def conv1D(arr, f):
    '''
    Applies filter on 1D signal by performing convolution

    Parameters
        arr (1D np array): input signal
        f (1D np array): filter
    Returns
        arr_filtered (1D np array): filtered version of input signal
    '''
    arr_copy = np.copy(arr)
    n = np.shape(arr_copy)[0]
    half_length = int(np.shape((f))[0]/2)

    #add padding based on filter size
    for i in range(half_length):
        arr_copy = np.insert(arr_copy, 0, 0)
        arr_copy = np.insert(arr_copy, len(arr_copy), 0)

    #convolve
    f_ = np.flip(f) #we flip filter for convolution
    arr_filtered = np.zeros((n,))
    for i in range(n):
        sum = 0
        for j in range(np.shape((f))[0]):
            sum += f_[j] * arr_copy[i+j]
        arr_filtered[i] = sum

    return arr_filtered

if __name__ == '__main__':
    a = np.array([0, 0, 0, 0, 5, 5, 5, 0, 0, 0])
    f = np.array([1, 0, -1]) #first deriv filter
    a_filtered = conv1D(a, f)
    print(a_filtered)

