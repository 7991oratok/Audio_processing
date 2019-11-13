# -*- coding: utf-8 -*-
import wave
import numpy as np
import matplotlib.pyplot as plt
import contextlib
import sys

args = sys.argv

# original data
fname = args[1]
name = "DATA/" + fname
wf1 = wave.open(name , "r" )
buf1 = wf1.readframes(wf1.getnframes())

# sil_cut data
tmp = fname.replace('.', '0.')
wf2 = wave.open("result/" + tmp , "r" )
buf2 = wf2.readframes(wf2.getnframes())

# バイナリデータを整数型（16bit）に変換
data1 = np.frombuffer(buf1, dtype="int16")
data2 = np.frombuffer(buf2, dtype="int16")

# グラフ化
plt.plot(data1)
plt.plot(data2)
plt.grid()
# plt.show()

fname_out = fname.replace('wav', 'png')
print('fig/' + fname_out)
plt.savefig('fig/' + fname_out)