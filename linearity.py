import numpy as np
N1=int(input("Enter number of points in the sequence-1: "))
N2=int(input("Enter number of points in the sequence-2: "))
x1=eval(input("Enter first sequence: "))
x2=eval(input("Enter second sequence: "))
a1=int(input("Enter the first constant: "))
a2=int(input("Enter the second constant: "))
if (N1>N2):
    L=N1
elif (N1<N2):
    L=N2
X1=np.zeros(N1,dtype=(complex))
X2=np.zeros(N2,dtype=(complex))
X3=np.zeros(L,dtype=(complex))
x3=np.zeros(L)
for i in range(0,N1):
    for j in range(0,N1):
        X1[i]=X1[i]+(x1[j]*np.exp(-2j*(np.pi)*j*i/N1))
for i in range(0,N2):
    for j in range(0,N2):
        X2[i]=X2[i]+(x2[j]*np.exp(-2j*(np.pi)*j*i/N2))
for i in range(0,L):
    x3[i]=a1*x1[i]+a2*x2[i]
for i in range(0,L):
    for j in range(0,L):
        X3[i]=X3[i]+(x3[j]*np.exp(-2j*(np.pi)*j*i/L))
print(x3)
print(X1)
print(X2)
print(X3)




