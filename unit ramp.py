import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,5,1)
y=[x1 for x1 in list(x)]
plt.subplot(121)
plt.plot(y) 
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('CTS Unit Ramp')
plt.subplot(122)
plt.stem(y)
plt.xlabel('n index')
plt.ylabel('amplitude')
plt.title('DTS Unit Ramp')
