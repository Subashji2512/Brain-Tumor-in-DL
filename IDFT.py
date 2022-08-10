import matplotlib.pyplot as plt
import numpy as np
N=(int(input("ENTER THE SIZE :")))
xn=[]
for n in range(N):
    xn.append(int(input()))
xk=0
f=[]
for k in range(N):
    for n in range(N):
        if(n==0):
            xk=xn[0]
        else:
            xk=xk+xn[n]*(np.exp(-2j*np.pi*n*k/N))
            x1=round(xk.real)
            y1=round(xk.imag)
            if(y1==0):
                z=x1
            else:
                z=x1+1j*y1
    f.append(z)

plt.subplot(221)
plt.stem(np.abs(f))
plt.title("magnitude")
plt.subplot(222)
plt.stem(np.angle(f))
plt.title("phase")
print(''.join(str(f).split(',')))

          
    