import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-2*np.pi,2*np.pi,0.1)
v1=np.sin(t)
plt.subplot(1,2,1)
plt.plot(t,v1)
plt.title("Sine wave CTS")
plt.xlabel("t")
plt.ylabel("v1")
n=np.arange(-2*np.pi,2*np.pi,0.5)
v2=np.sin(n)
plt.subplot(1,2,2)
plt.stem(n,v2)
plt.title("Sine wave DTS") 
plt.xlabel("n")
plt.ylabel("v2")

