import matplotlib.pyplot as plt
import numpy as np
N=int(input("Enter the length of the sequence: "))
x=np.zeros(N)
print("Enter the elements of the sequence: ")
for i in range(N):
    x[i]=int(input())
    
def even_x(x):
    n=np.arange(int(len(x)/2))
    y=np.zeros(int(len(x)/2))
    for i in range(len(n)):
        y[i]=x[2*i]
    return y

def odd_x(x):
    n=np.arange(int(len(x)/2))
    y=np.zeros(int(len(x)/2))
    for i in range(len(n)):
        y[i]=x[2*i+1]
    return y
g=even_x(x)
h=odd_x(x)
print("g[n] = ",g)
print("h[n] = ",h) 
  
def DFTX(x):
    N = len(x)
    n = np.arange(N) 
    k = n.reshape(N,1) 
    Wn = np.exp(-2j*np.pi*k*n/N)
    X = np.dot(Wn,x) 
    return X
G=DFTX(g)
H=DFTX(h)
print("G[K] = ",np.round(G,2))
print("H[K] = ",np.round(H,2))

X=np.zeros(N,dtype=np.complex_)
for i in range(N):
    if i<int(N/2):
        X[i]=G[i]+np.exp(-2j*np.pi*i/N)*H[i]
    else:
        X[i]=G[i-int(N/2)]+np.exp(-2j*np.pi*i/N)*H[i-int(N/2)]
print("X[K] = ",np.round(X,3))

plt.subplot(2,3,1)
plt.stem(G)
plt.title("G[K]")
plt.subplot(2,3,3)
plt.stem(H)
plt.title("H[K]")
plt.subplot(2,3,4)
plt.stem(np.abs(X))
plt.title("MAGNITUDE OF X[K]")
plt.xlabel("Real")
plt.ylabel("Imag")
plt.subplot(2,3,6)
plt.stem(np.angle(X))
plt.title("PHASE OF X[K]")
plt.xlabel("Real")
plt.ylabel("Imag")

         









