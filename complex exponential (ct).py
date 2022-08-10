import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(-0.02,0.05,50)
plt.subplot(4,1,1);
plt.plot(t,np.exp(2j*np.pi*50*t).real)
plt.xlabel("t")
plt.ylabel("Real : x(t)")
plt.title("Complex Exponential signal CTS")
plt.subplot(4,1,2);
plt.plot(t,np.exp(2j*np.pi*50*t).imag)
plt.xlabel("t")
plt.ylabel("Imaginary : x(t)")
n = np.linspace(-0.02,0.05,50)
plt.subplot(4,1,3);
plt.stem(n,np.exp(2j*np.pi*50*n).real)
plt.xlabel("n")
plt.ylabel("Real : x[n]")
plt.title("Complex Exponential signal DTS")
plt.subplot(4,1,4);
plt.stem(n,np.exp(2j*np.pi*50*n).imag)
plt.xlabel("n")
plt.ylabel("Imaginary : x[n]")

