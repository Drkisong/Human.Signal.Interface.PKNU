## Import mordule
import numpy as np
import matplotlib.pyplot as plt

## Data load
n_file = 'emg_data.csv'
emg = np.loadtxt(n_file , delimiter = ',')
data = emg[:,1]
data_time = emg[:,0]

## Date plot
plt.plot(data_time, data)
plt.title('Raw data (EMG)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitue (v)')
plt.show()
