## Import mordule
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp
from scipy import signal
import scipy.fft

## Data load
n_file = 'emg_data.csv'
emg = np.loadtxt(n_file , delimiter = ',')
data = emg[:,1]
data_time = emg[:,0]

## Input parameters
s_rate = 0.00008  #unit [sec]
n_samples = len(data) 
d_time = np.arange(n_samples)*s_rate

## Data plot
plt.plot(d_time, data)
plt.title('Raw data (EMG)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitue (v)')
plt.show()

## Absolute value of EMG
d_offset = 1.65
d_offset_data = data-d_offset
abs_data = np.abs(d_offset_data)
plt.plot(d_time, abs_data)
plt.title('Absolute value (EMG)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitue (v)')
plt.show()

analystic_emg = hilbert(d_offset_data)
amplitude_envlope = np.abs(analystic_emg)
plt.plot(d_time, analystic_emg)
plt.title('analystic_emg (EMG)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitue (v)')
plt.show()

plt.plot(d_time, amplitude_envlope)
plt.title('amplitude_envlope (EMG)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitue (v)')
plt.show()

## FFT
y_f = np.fft.fft(d_offset_data)
x_f = np.linspace(0.0,1.0/(2.0*s_rate),n_samples//2)

plt.plot(x_f,2.0/n_samples*np.abs(y_f[:n_samples//2]))
plt.title('FFT')
plt.xlabel('Frequency (Hz)')
plt.show()

plt.plot(x_f,2.0/n_samples*np.abs(y_f[:n_samples//2]))
plt.title('FFT_scale')
plt.xlim([0, 500])
plt.xlabel('Frequency (Hz)')
plt.show()

## STFT
f, t, Zxx = signal.stft(data, 1/s_rate, nperseg=2**10)
plt.pcolormesh(t, f, np.abs(Zxx),shading='gouraud')
plt.title('STFT Magnitude of emg')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (sec)')
plt.ylim(0, 500)
plt.show()

f, tt, Sxx = signal.spectrogram(data, 1/s_rate, window=('tukey',0.1))
plt.pcolormesh(tt, f, np.abs(Sxx), shading='gouraud')
plt.title('Spectrogram of emg')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.ylim(0, 500)
plt.show()

## MAV
def mov_avg_filter(x_n, x_meas):
    """이동평균 계산 (배치식)."""
    n = len(x_n)
    for i in range(n-1):
        x_n[i] = x_n[i+1]
    x_n[n-1] = x_meas
    x_avg = np.mean(x_n)
    return x_avg, x_n

x_meas_save = np.zeros(n_samples)
x_avg_save = np.zeros(n_samples)
n_win = 200

for i in range(n_samples):
    x_meas = abs_data[i]
    if i == 0:
        x_avg, x_n = x_meas, x_meas * np.ones(n_win)
    else:
        x_avg, x_n = mov_avg_filter(x_n, x_meas)
 
    x_meas_save[i] = x_meas
    x_avg_save[i] = x_avg

plt.plot(d_time, x_meas_save, 'r-', label='Measured')
plt.plot(d_time, x_avg_save, 'b-', label='Moving average')
plt.legend(loc='upper left')
plt.title('Measured signals v.s. Moving Average Filter Values')
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude (V)')
plt.show()
