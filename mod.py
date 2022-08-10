import numpy as np
import math
import matplotlib.pyplot as plt

def dft(x):
    N = len(x)
    y = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            y[k] += x[n] * np.conj(complex(math.cos(2 * np.pi * k * n / N), math.sin(2 * np.pi * k * n / N)))
    return y

def create_sequence():
    N = int(input(f"Enter the length of input sequence:"))
    y = np.zeros(N, dtype=complex)
    for index in range(N):
        y[index] = complex(input(f"Enter the value of sequence at index{index} for Q1:"))
    return y

def splitting_fun(x):
    g = np.zeros(int(len(x)/2), dtype = complex)
    h = np.zeros(int(len(x)/2), dtype = complex)
    c1 = 0
    c2 = 0
    for index in range(0, len(x)):
        if index%2 == 0:
            g[c1] = x[index]
            c1 += 1
        else:
            h[c2] = x[index]
            c2 += 1
    return np.array([g, h])

def dft2(x):
    N = len(x)
    X = np.zeros(N, dtype = complex)
    g = splitting_fun(x)[0]
    h = splitting_fun(x)[1]
    G = np.append(dft(g), dft(g))
    H = np.append(dft(h), dft(h))
    for k in range(N):
        X[k] = G[k] + H[k] * np.conj(complex(math.cos(2*np.pi*k/N), math.sin(2*np.pi*k/N)))
    return np.array([X, G, H])
        
x = create_sequence()
G = dft2(x)[1]
H = dft2(x)[2]
X = dft2(x)[0]
plt.subplot(3,1,1)
plt.xlabel('real axis')
plt.ylabel('imag axis G[k]')
plt.stem(G.real, G.imag)
plt.subplot(3,1,2)
plt.xlabel('real axis')
plt.ylabel('imag axis H[k]')
plt.stem(H.real, H.imag)
plt.subplot(3,1,3)
plt.xlabel('real axis')
plt.ylabel('Imag axis X[k]')
plt.stem(X.real, X.imag)
plt.show()