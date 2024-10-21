## Import mordule
import numpy as np
import matplotlib.pyplot as plt

## Data load
f_dir = '2023_HMI'
n_file = '2023_HMI/emg_data.csv'
emg = np.loadtxt(n_file , delimiter = ',')
data = emg[:,1]
data_time = emg[:,0]

## Date plot
plt.plot(data_time, data)
plt.title('Raw data (EMG)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitue (v)')
plt.show()
