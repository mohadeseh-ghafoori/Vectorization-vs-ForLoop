import numpy as np
import time
#vectorization method for inner product of 2 vector 
a=np.random.rand(10000000)
b=np.random.rand(10000000)
tic=time.time()
c=np.dot(a,b)
toc=time.time()
print("vectorized version: "+ str(1000*(toc-tic)) +" ms")
#for loop method 
c=0
tic=time.time()
for i in range(10000000):
    c+=a[i]*b[i]
toc=time.time()
print("for loop version: "+ str(1000*(toc-tic)) +" ms")
