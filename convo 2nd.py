import matplotlib.pyplot as plt
import numpy as np
def delfun(x):
    t=(x==0)
    t=1*t
    return t
def h(n2):
    t2=2*delfun(n2)+delfun(n2-1)
    return t2
n=np.arange(-2,6,1)
xn=delfun(n)+delfun(n-1)+delfun(n-2)
yn=h(n)+h(n-1)+h(n-2)
plt.subplot(1,5,1)
plt.xlabel("n index")
plt.ylabel("x")
plt.title("x[n]")
plt.stem(n,xn)
plt.subplot(1,5,3)
plt.xlabel("n index")
plt.ylabel("h")
plt.title("h[n]")
plt.stem(n,h(n))
plt.subplot(1,5,5)
plt.xlabel("n index")
plt.ylabel("y")
plt.title("y[n]")
plt.stem(n,yn)