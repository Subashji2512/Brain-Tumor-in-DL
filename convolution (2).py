import matplotlib.pyplot as plt
import numpy as np
x=([1,1,1,0])
h=([2,1,0,0])
l=len(x)
plt.subplot(1,3,1)
plt.xlabel("n index")
plt.ylabel("x")
plt.title("x[n]")
plt.stem(x)
plt.subplot(1,3,2)
plt.xlabel("n index")
plt.ylabel("h")
plt.title("h[n]")
plt.stem(h)
v=np.zeros(l)
for i in range(0,l):
    for j in range(0,l):
        if(i-j)>=0:
            v[i]=v[i]+x[j]*h[i-j]
plt.subplot(1,3,3)
plt.xlabel("n index")
plt.ylabel("y")
plt.title("y[n]")
plt.stem(v)
y=np.convolve(x,h)
print(y)
        

