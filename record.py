# -*- coding: utf-8 -*-
import pyaudio
import sys
import time
import wave
import requests
import os
import json
import numpy as np
from datetime import datetime
import subprocess
import pathlib

# 音声録音
def recognize_rec():

    chunk = 1024
    threshold = 0.002
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    STOP_SECONDS = 1  # レコード後の無音区間の継続時間
    RECORD_SECONDS = 10 # レコード時間の最大値

    A = int(RATE) / int(chunk) * int(RECORD_SECONDS)
    B = int(RATE / chunk * STOP_SECONDS)
    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = chunk)

    
    print("RATE = " + str(RATE))
    print("chunk = " + str(chunk))
    print("RECORD_SECONDS = " + str(RECORD_SECONDS))
    print("RATE / chunk * RECORD_SECONDS = " + str(A))
    print("")

    cnt = 0

    while True:
        data = stream.read(chunk)
        x = np.frombuffer(data, dtype="int16") / 32768.0

        #まずサンプルを取る！
        xmax = x.max()

        if xmax > threshold: #録音レベルがしきい値を上回ったら
            filename = datetime.today().strftime("%Y%m%d%H%M%S") + ".wav"
            print(cnt, filename)
            all = []
            n = 0
            for _ in range(0, int(A)): 
                data = stream.read(chunk)
                all.append(data)
                x = np.frombuffer(data, dtype="int16") / 32768.0
                xmax = x.max()

                if xmax <= threshold:
                    n += 1
                else:
                    n = 0
                # 中断判定
                if n == B:
                    break

            data = b''.join(all)
            out = wave.open("result/" + filename,'w')
            out.setnchannels(1) #mono
            out.setsampwidth(2) #16bits
            out.setframerate(RATE)
            out.writeframes(data)
            out.close()
            cnt += 1

        if cnt > 5 : 
            print("Recording done.")
            break      

    stream.close() 
    p.terminate()

# result内のwavファイル名を取得
# scriptファイルに hoge.wav hoge.mfc ... を書き込み
def script_hcopy():

    wavefiles = []
    all = pathlib.Path('2019_12_result/').glob('*.wav')
    for f in all:
        wavefiles.append(f.name)

    fname = "2019_12_result/script.hcopy"
    fname2 = "input.sh"

    file = open(fname, 'w')
    file2 = open(fname2 ,'w')
    
    for i in range(len(wavefiles)):
        tmp = wavefiles[i].replace('.wav', '')
        file.write('2019_12_result/' + tmp + '.wav 2019_12_result/' + tmp + '.mfc\n')
        file2.write('HList -r 2019_12_result/' + tmp + '.mfc > 2019_12_MFCC_DATA/' + tmp + '.txt\n')


    file.close()

    print("Writing done.")

# HCopy 実行
def hcopy():
    subprocess.run('HCopy -C 2019_12_result/config.hcopy -S 2019_12_result/script.hcopy', shell=True)
    print("HCopy done.")

def hlist():
    subprocess.run('bash input.sh', shell=True)
    print("HList done.")

if __name__ == '__main__':
    
    # print(recognize_rec())
    # script_hcopy()
    # hcopy()
    hlist()
