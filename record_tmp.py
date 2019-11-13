# -*- coding: utf-8 -*-
#マイク0番からの入力を受ける。録音し、保存する。

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

def recognize_rec():
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1

    CARD = 1 #OUTPUTの指定
    DEVICE = 0 #OUTPUTの指定
    threshold = 0.002 #しきい値
    #サンプリングレート、マイク性能に依存
    RATE = 16000
    STOP_SECONDS = 1  # [sec]
    B = int(RATE / chunk * STOP_SECONDS)
    #録音時間の上限
    RECORD_SECONDS = 10

    #pyaudio
    p = pyaudio.PyAudio()
    #マイク0番を設定
    input_device_index = 0
    #マイクからデータ取得
    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = chunk)

    
    

    A = int(RATE) / int(chunk) * int(RECORD_SECONDS)

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
            for i in range(0, int(A)): #←抜けたいfor構文！
                data = stream.read(chunk)
                all.append(data)
                x = np.frombuffer(data, dtype="int16") / 32768.0
                xmax = x.max()
                if xmax <= threshold:
                    # 閾値を下回っていたらincrementする
                    n += 1
                else:
                    # 閾値を上回ったらリセットする
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

            
        if cnt > 5 : break


        #time.sleep(0.5)         

    stream.close() 
    p.terminate()


if __name__ == '__main__':
    print(recognize_rec())
    print("Recording finished.")
    subprocess.run('HCopy')
