# Ex1

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for interactive plotting

# N = 1000
# sigma = 1
#
# fSignal = np.zeros(N)
# fNoise = np.random.normal(0, sigma, N)
#
# for i in range(1, N):
#     fSignal[i] = fSignal[i-1] + fNoise[i]
#
# plt.plot(fNoise, label='Noise')
# plt.plot(fSignal, label='Signal', color='orange')
# plt.legend()
# plt.grid()
# plt.show()

# Ex 2

N = 1000
sigma = 5
r = 0.99
en = np.sqrt((1-r*r)*sigma*sigma)

fSignal = np.zeros(N)
fSignal[0] = np.random.normal(0, sigma)
for i in range(1, N):
    fSignal[i] = r * fSignal[i-1] + np.random.normal(0, en)

plt.plot(fSignal, label='Signal', color='orange')
plt.grid()
plt.show()