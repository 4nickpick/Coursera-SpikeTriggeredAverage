"""
Created on Wed Apr 22 15:15:16 2015

Quiz 2 code.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

import pickle

from compute_sta import compute_sta


FILENAME = 'c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)


# the stimulus and the neural response our recorded at the exact same time intervals
# so, the stimulus and neural responses and can be mapped together

# stimulus time series
stim = data['stim']

# spike-train time series, ρ
rho = data['rho']


# The recording rate of the current data set is 500 Hz, therefore our sampling period is 2ms (1000 / 500)
sampling_period = 2   # in ms

# We're using 300 ms windows to calculate our spike-triggered average
# So, we need 150 timesteps to look back through (300 / 2)
num_timesteps = 150

# Our spike-triggered average calculations
sta = compute_sta(stim, rho, num_timesteps)

# Calculating our x-axis values (time intervals)
time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

# generate and show the graph
plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')
plt.show()
