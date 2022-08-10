import numpy as np

N=int(input("Enter number of points in sequence: "))
x=eval(input("Enter sequence: "))
Fshift=int(input("Enter shift value: "))
xn=np.zeros(N,dtype=(complex))
X=np.zeros(N,dtype=(complex))
Xn=np.zeros(N,dtype=(complex))
for i in range(N):
    xn[i]=x[i]*np.exp(2j*np.pi*i*Fshift/N)
print("time domain sequence")

for k in range (N):
    for n in range(N):
        X[k]=X[k]+x[n]*np.exp(-2j*np.pi*k*n/N)
for k in range (N):
    for n in range(N):
        Xn[k]=Xn[k]+xn[n]*np.exp(-2j*np.pi*k*n/N)
print("shifted output X[k-1]")
print(np.round(X,2))
print("X[k]")
print(np.round(Xn,2))