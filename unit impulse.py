import numpy as np
import matplotlib.pyplot as plt
n=np.arange(-10,10,1)
b=len(n)
v=np.zeros(b)
v[0]=0
for i in range(0,b):
 if(n[i]==0):
  v[i]=1
 else:
  v[i]=0 
plt.subplot(3,1,1)
plt.stem(n,v)
plt.title("del[n]")
plt.xlabel("n")
plt.ylabel("v")
for i in range(0,b):
 if(n[i]==5):
  v[i]=2
 else: 
  v[i]=0
plt.subplot(3,1,2)
plt.stem(n,v)  
plt.title("2del[n-5]")
plt.xlabel("n")
plt.ylabel("v")
for i in range(0,b):
 if(n[i]==0):
  v[i]=1
 elif(n[i]==5):
  v[i]=2
 else:
  v[i]=0
plt.subplot(3,1,3)
plt.stem(n,v)
plt.title("del[n]+ 2del[n-5]")
plt.xlabel("n")
plt.ylabel("v")