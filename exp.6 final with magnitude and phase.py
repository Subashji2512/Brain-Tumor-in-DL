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

plt.subplot(8,3,1)
plt.stem(np.abs(G))
plt.title("mag of G[K]")
plt.subplot(8,3,3)
plt.stem(np.angle(G))
plt.title("phase of G[K]")
plt.subplot(8,3,7)
plt.stem(np.abs(H))
plt.title("mag of H[K]")
plt.subplot(8,3,9)
plt.stem(np.angle(H))
plt.title("phase of H[K]")
plt.subplot(8,3,13)
plt.stem(np.abs(X))
plt.title("MAGNITUDE OF X[K]")
plt.xlabel("Real")
plt.ylabel("Imag")
plt.subplot(8,3,15)
plt.stem(np.angle(X))
plt.title("PHASE OF X[K]")
plt.xlabel("Real")
plt.ylabel("Imag")

def DFT1(x,N):

 
    n = np.arange(N)
    k = n.reshape((N, 1))
    Wn = np.exp(-2j * np.pi * k * n / N)
    
    print("The W_N matrix is \n",np.round(Wn,2))
    X = np.dot(Wn, x)
    return X

size =N
x1=[]
N1 = N
if(N1<len(x)):
    for i in range(N1):
        x1.append(x[i])
elif(N1>len(x)):
    x1 = x
    for i in range(N1-size):
        x1.append(0)
else:
    x1 = x
X = DFT1(x1,N1)
N = len(X)
n = np.arange(0,N)
Y = np.zeros(N,dtype=np.complex_)
for i in range(0,len(X)):
    Y[i]=np.round(X[i],2)

print("the DFT using linear transform is")    
print("\n\n",Y)



plt.subplot(8,3,19)
plt.stem(np.abs(Y))
plt.xlabel('Real')
plt.ylabel('Imaginary')


plt.subplot(8,3,21)
plt.stem(np.angle(Y))
plt.xlabel('Real')
plt.ylabel('Imaginary')



        
