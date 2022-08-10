import numpy as np
N=int(input("Enter the number of point DFT: "))
x=eval(input("Enter the sequence: "))
L=int(input("Enter shift: "))
x1=np.zeros(N)
X=np.zeros(N,dtype=(complex))
X1=np.zeros(N,dtype=(complex))
for k in range(N):
    for n in range(0,N):
        X[k]=X[k]+(x[n]*(np.exp(-2j*(np.pi)*k*n/N)))
for k in range(N):
    X1[k]=X[k]*(np.exp(-2j*(np.pi)*k*L/N))
for k in range(N):
    for n in range(N):
       x1[k]=x1[k]+(1/N)*(X1[n]*(np.exp(2j*(np.pi)*k*n/N)))
print(x)
print(np.round(X))
print(x1)
print(np.round(X1))