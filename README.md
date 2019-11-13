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

開発途中