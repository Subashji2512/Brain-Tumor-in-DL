import matplotlib.pyplot as plt
import numpy as np

plt.subplot(121)
x = np.arange(0,10,1)
y = np.exp(x)
plt.title("Continuous time exponential")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(x,y)

plt.subplot(122)
plt.title("discrete time exponential")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.stem(x,y)
