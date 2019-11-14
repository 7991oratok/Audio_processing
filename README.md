# 音声前処理

## audio.py
DATA内の音声の無音区間処理を行うプログラム

    python audio.py [wav file name]


## waveform.py
DATAにある元wavデータとaudio.pyで無音区間処理した後のwavデータを
グラフ化してfigに保存するプログラム

    python waveform.py

## record.py
指定された閾値以上の音声が流れてきたら録音するプログラム
1. 閾値以上の音声が流れてきたら音声を録音する。
2. 閾値以下の音声が一定以上続いたら録音を終了し、wavファイルをresult/に保存する。
3. 1,2を数回繰り返した後、result/フォルダ内のwavファイルから.mfcファイルを作成する。
4. 3で作成した.mfcファイルをもとに.txtファイルを作成する。