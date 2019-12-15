import sys

import numpy as np
import scipy.fftpack as fft
import matplotlib.pyplot as plt
import wave
import audioop
import soundfile as sf

outf = 'tmp_DATA/test.wav'
filename = 'tmp_DATA/migi_itte0.wav'

wav,samplerate = sf.read(filename)
# wav = wave.open(filename)
data = audioop.tostereo(wav,2,0.5,0.5)
print(type(data))

# sf.write('new_file.wav', data, samplerate)


