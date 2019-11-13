# -*- coding: utf-8 -*-
from pydub import AudioSegment
from pydub.silence import split_on_silence
import sys

args = sys.argv

# wavファイルのデータ取得
fname = args[1].replace('.wav', '')
sound = AudioSegment.from_file("DATA/" + fname + ".wav", format="wav")


# wavデータの分割（無音部分で区切る）
# パラメータは適宜調整
chunks = split_on_silence(sound, min_silence_len=1500, silence_thresh=-500, keep_silence=100)

# 分割したデータ毎にファイルに出力
for i, chunk in enumerate(chunks):
    chunk.export("result/" + fname  + str(i) +".wav", format="wav")


print('Audio processing finished. (file:',fname,')')
print('Sliced number : ',i+1)