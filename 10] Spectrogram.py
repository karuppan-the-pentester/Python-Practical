import matplotlib.pyplot as plot
from scipy.io import wavfile
samplingFrequency, signalData = wavfile.read('male.wav')
plot.subplot(211)
plot.title('Spectrogram of a wav file with piano music')
plot.plot(signalData)
plot.xlabel('Sample')
plot.ylabel('Amplitude')
plot.subplot(212)
plot.specgram(signalData, Fs=samplingFrequency)
plot.xlabel('Time')
plot.ylabel('Frequency')
plot.show()