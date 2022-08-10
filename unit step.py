import numpy as np
import matplotlib.pyplot as plt
x=np.ones(10)
plt.subplot(121)
plt.plot(x)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('continous unit step fn')
plt.subplot(122)
plt.stem(x)
plt.xlabel('n index')
plt.ylabel('amplitude')
plt.title('discrete unit step fn')

