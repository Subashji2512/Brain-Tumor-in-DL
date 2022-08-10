import matplotlib.pyplot as plt
import numpy as np
def DFT1(x,N):

 
    n = np.arange(N)
    k = n.reshape((N, 1))
    Wn = np.exp(-2j * np.pi * k * n / N)
    
    print("The W_N matrix is \n",np.round(Wn,2))
    X = np.dot(Wn, x)
    return X

size = int(input("Enter the size : "))
x1 = []
x = []
for i in range(size):
    x1.append(int(input()))
    
N1 = int(input("Enter the size of N : "))
if(N1<len(x1)):
    for i in range(N1):
        x.append(x1[i])
elif(N1>len(x1)):
    x = x1
    for i in range(N1-size):
        x.append(0)
else:
    x = x1
X = DFT1(x,N1)
N = len(X)
n = np.arange(0,N)
Y = np.zeros(N,dtype=np.complex_)
for i in range(0,len(X)):
    Y[i]=np.round(X[i],2)
    
print("\n\n",Y)



plt.subplot(221)
plt.stem(np.abs(Y))
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('DFT Linear Transformation')

plt.subplot(224)
plt.stem(np.angle(Y))
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('DFT Linear Transformation')
