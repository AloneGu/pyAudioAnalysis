import wave
import numpy as np
import matplotlib.pyplot as plt


# Created input file with:
# mpg123  -w 20130509talk.wav 20130509talk.mp3
wr = wave.open('./audio_data/count2.wav', 'r')
par = list(wr.getparams()) # Get the parameters from the input.
# This file is stereo, 2 bytes/sample, 44.1 kHz.
par[3] = 0 # The number of samples will be set by writeframes.

# Open the output file
ww = wave.open('./output/filtered-talk.wav', 'w')
ww.setparams(tuple(par)) # Use the same parameters as the input file.

lowpass = 80 # Remove lower frequencies.
highpass = 800 # Remove higher frequencies.

sz = wr.getframerate() # Read and process 1 second at a time.
c = int(wr.getnframes()/sz) # whole file
for num in range(c):
    print('Processing {}/{} s'.format(num+1, c))
    da = np.fromstring(wr.readframes(sz), dtype=np.int16)
    left, right = da[0::2], da[1::2] # left and right channel
    #plt.subplot(2,1,1)
    #plt.plot(left)
    lf, rf = np.fft.rfft(left), np.fft.rfft(right)
    lf[:lowpass], rf[:lowpass] = 0, 0 # low pass filter
    #lf[55:66], rf[55:66] = 0, 0 # line noise
    lf[highpass:], rf[highpass:] = 0,0 # high pass filter

    lf = lf*1.5
    rf = rf*1.5

    nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
    #plt.subplot(2,1,2)
    #plt.plot(lf)
    #plt.show()
    ns = np.column_stack((nl,nr)).ravel().astype(np.int16)
    ww.writeframes(ns.tostring())
# Close the files.

wr.close()
ww.close()