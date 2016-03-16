from pylab import plot,xlabel,ylabel,arange,show,fft,ceil,log10
import matplotlib.pyplot as plt
from scipy.io import wavfile

filename = './audio_data/count2.wav'
sampFreq, snd = wavfile.read(filename)
print 'type',snd.dtype
print 'shape',snd.shape

print len(snd)
snd = snd[:10000]
print len(snd)
snd = snd / (2.**15)
sample_points = 10000.0


s1 = snd
samp_freq =  44100
timeArray = arange(0, sample_points, 1)
timeArray = timeArray / samp_freq
timeArray = timeArray * 1000

plt.figure(1)
plt.subplot(211)
plt.plot(timeArray, s1, color='k')
ylabel('Amplitude')
xlabel('Time (ms)')


n = len(s1)
p = fft(s1)
nUniquePts = ceil((n+1)/2.0)
p = p[0:nUniquePts]
p = abs(p)
p = p / float(n) # scale by the number of points so that
                 # the magnitude does not depend on the length
                 # of the signal or on its sampling frequency


# multiply by two (see technical document for details)
# odd nfft excludes Nyquist point
if n % 2 > 0: # we've got odd number of points fft
    p[1:len(p)] = p[1:len(p)] * 2
else:
    p[1:len(p) -1] = p[1:len(p) - 1] * 2 # we've got even number of points fft

freqArray = arange(0, nUniquePts, 1.0) * (sampFreq / n)
plt.subplot(212)
plt.plot(freqArray/1000, 20*log10(p), color='k')
xlabel('Frequency (kHz)')
ylabel('Power (dB)')
show()
