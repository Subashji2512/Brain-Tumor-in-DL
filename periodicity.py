import numpy as np
import matplotlib.pyplot as mpl
N=int(input("Enter number of points in the sequence: "))
x=eval(input("Enter the points: "))
X=np.zeros(N,dtype=(complex))
X1=np.zeros(N,dtype=(complex))
for i in range(0,N):
    for j in range(0,N):
        X[i]=X[i]+(x[j]*np.exp(-2j*(np.pi)*j*i/N))
for i in range(0,N):
    for j in range(0,N):
        X1[i]=X1[i]+(x[j]*np.exp(-2j*(np.pi)*j*(i+N)/N))
print(np.round(X))
print(np.round(X1))
mpl.subplot(331)
mpl.stem(X)
mpl.subplot(333)
mpl.stem(X1)