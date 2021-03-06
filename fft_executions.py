# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# https://helve-python.hatenablog.jp/entry/2018/06/17/000000


df = pd.read_csv('../bfs-x_data/bitflyer_executions/2020_03/Exec_2020_03_22.csv', names=('exec_date', 'jst_epoc', 'side', 'price', 'size', 'id', 'latency') ) # CSVファイル読み込み

df = df.drop(
    df.index[df.exec_date == 'Connection is already closed.']).dropna()  # 不要行の除去

# Pandas SeriesからNumpy Ndarrayへ変換
prices = df.price.values

n = len(prices)
print(f'{n} executions')

# とりあえずプロット
fig, ax = plt.subplots()
ax.plot(prices)
# ax.set_xlim(0, 0.1)
# ax.set_xlabel("Time [s]")
# ax.set_ylabel("Signal")
# ax.grid()
plt.show()

# N = 1024            # サンプル数
# dt = 0.001          # サンプリング周期 [s]
# f1, f2 = 50, 120    # 周波数 [Hz]

# t = np.arange(0, N*dt, dt) # 時間 [s]
# x = 1.5*np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t) + 3 # 信号

# fig, ax = plt.subplots()
# ax.plot(t, x)
# # ax.set_xlim(0, 0.1)
# ax.set_xlabel("Time [s]")
# ax.set_ylabel("Signal")
# ax.grid()
# plt.show()

# # 関数numpy.fft.fft()によりフーリエ変換を行う。
F = np.fft.fft(prices) # 変換結果

# フーリエ変換の周波数を取得
freq = np.fft.fftfreq(n, d=1) # 周波数

# fig, ax = plt.subplots(nrows=3, sharex=True, figsize=(6,6))
# ax[0].plot(F.real, label="Real part")
# ax[0].legend()
# ax[1].plot(F.imag, label="Imaginary part")
# ax[1].legend()
# ax[2].plot(freq, label="Frequency")
# ax[2].legend()
# ax[2].set_xlabel("Number of data")
# plt.show()


# 元の信号の振幅を求める。
Amp = np.abs(F/(n/2)) # 振幅

fig, ax = plt.subplots()
ax.set_xlim(0, 0.1)
ax.plot(freq[1:int(n/2)], Amp[1:int(n/2)])
ax.set_xlabel("Freqency [Hz]")
ax.set_ylabel("Amplitude")
ax.grid()
plt.show()