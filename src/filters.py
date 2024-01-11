# Import Libraries
import numpy as np
import cv2 as cv
from math import pi, exp, sqrt

#image to audio conversion
def audio2img(arr):
    '''
    Scales the input audio (with values from -1 to 1) to have values between 0-255
    Parameters
        arr (2D np array): input audio
    Returns
        arr_norm (2D np array): normalized image
    '''
    return (arr + 1)*255/2

def img2audio(arr):
    '''
    Scales the input img (with values from 0 to 255) to have values between -1 to 1
    Parameters
        arr (2D np array): input img
    Returns
        arr_norm (2D np array): scaled audio
    '''
    return arr*(2/255)-1

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

def gauss1D(size, sigma):
    '''
    Parameters
        size (size): size of filter
        sigma (float): standard deviation
    Returns
        f (1D np array): Gaussian filter
    '''
    f = np.zeros(size)
    cst = 1/(sqrt(2*pi)*sigma)
    half_length = int(size/2)
    sum = 0

    for i in range(size):
        n = cst*exp(-((i-half_length)**2)/(2*sigma**2))
        f[i] = n
        sum += n

    #normalize
    f = 1/sum * f

    return f

#manual Gaussian filter
def gauss2D(size, sigma):
    '''
    Parameters
        size (size): size of filter
        sigma (float): standard deviation
    Returns
        f (2D np array): Gaussian filter
    '''
    f = np.zeros((size, size))
    cst = 1/(2*pi*sigma**2)
    half_length = int(size/2)
    sum = 0

    for i in range(size):
        for j in range(size):
            n = cst*exp(-((i-half_length)**2 + (j-half_length)**2)/(2*sigma**2))
            f[i, j] = n
            sum += n

    #normalize
    f = 1/sum * f

    return f


#testing
if __name__ == '__main__':
    #testing manual 1D filtering function
    a = np.array([0, 0, 0, 0, 5, 5, 5, 0, 0, 0])
    f = np.array([1, 0, -1]) #first deriv filter
    a_filtered = conv1D(a, f)
    print(a_filtered)

    #testing manual gaussian function
    gauss = gauss2D(5, 5)
    print(gauss)

    gauss1 = gauss1D(5, 1)
    print(gauss1)

    #testing audio to img conversion
    img = np.array([0, 255, 127.5])
    print(img2audio(img))

    audio = np.array([-1, 1, 0])
    print(audio2img(audio))

    #test img for convolution testing
    test_arr = np.zeros((256, 256))

    #create line
    for i in range(0, 255):
        test_arr[50, i] = 255
        test_arr[51, i] = 255
        test_arr[100, i] = 255
        test_arr[101, i] = 255
        test_arr[200, i] = 255
        test_arr[201, i] = 255
    
    #gaussian blur using 2D conv function
    test_arr_filt = cv.filter2D(src=test_arr, ddepth=-1, kernel=gauss) #ddepth of -1 means same img depth as input img

    #gaussian blur using gaussian function
    test_arr_filt2 = cv.GaussianBlur(src=test_arr, ksize=(5,5), sigmaX=5)

    #cv.imwrite('test_filt.bmp', test_arr_filt)
    #cv.imwrite('test_filt2.bmp', test_arr_filt2)




    


