import numpy as np
import matplotlib.pyplot as plt
def DFTX(x):

    N = len(x)
    X = np.zeros(N,dtype=np.complex_)
    for k in range(N):
        for n in range(N):
            e = np.exp(-2j * np.pi * k * n / N)
            X[k]=X[k]+x[n]*e
    return X

def IDFTX(X):

    N = len(X)
    x = np.zeros(N,dtype=np.complex_)
    for n in range(N):
        for k in range(N):
            e = np.exp(2j * np.pi * k * n / N)
            x[n]=x[n]+X[k]*e
    x=np.multiply((1/N),x)
    return x.real

h=[]
x=[]
f=int(input("enter the num of x values:"))
for i in range(0,f):
    x.append(int(input()))
a=int(input("enter the num of h values:"))
for i in range(0,a):
    h.append(int(input()))
L=5
M=len(h)
N=L+M-1
h2=np.zeros(N)
for i in range (0,len(h)):
    h2[i]=h[i]

m=int(np.ceil(len(x)/L))

print ("h[n] : ",h2)

le=len(x)+len(h)-1
y=np.zeros(le)
position=0
pos2=0
for i in range (0,m):
    xt=np.zeros(N)
    Y= np.zeros(N)
    for k in range(0,L):
        xt[k]=x[position+k]
    print("xt[n] : ",xt)
    
    Y= np.round(IDFTX(np.multiply(DFTX(xt),DFTX(h2))),0)
    print("Y ",Y)
    if(i==0):
        for k in range (0,N):
            y[k]=Y[k]
    else:
        for k in range(0,N):
            y[pos2-M+1+k]+=Y[k]            
    position+=L
    pos2+=N

print("y[n] : ",y)

y2=np.convolve(x,h)
print(y2)

plt.figure(figsize = (12,9))
n=np.arange(0,le)
plt.subplot(2,2,1)
plt.stem(n,y)
plt.xlabel('time index')
plt.ylabel('y[n]')
plt.title('Overlap Add')