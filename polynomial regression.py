import random
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.array([math.log10(1), math.log10(9), math.log10(22),
              math.log10(24), math.log10(25), math.log10(26),
              math.log10(27), math.log10(28), math.log10(29),
              math.log10(30), math.log10(31), math.log10(32), 
              math.log10(33), math.log10(34), math.log10(35)])
y = np.array([math.log10(8), math.log10(9), math.log10(51), 
              math.log10(115), math.log10(164), math.log10(209),
              math.log10(278), math.log10(321), math.log10(382),
              math.log10(456), math.log10(596), math.log10(798),
              math.log10(1140), math.log10(1174), math.log10(1543)])
c = random.random()

plt.scatter(x, y)

n = 5

m=[]
x_real = []
alpha = 0.0001
y_hat = []

for i in range(1, n+1):
    x_real.append(x**i)
    m.append(random.random())
    
x_real = np.array(x_real)
m = np.array(m)

x_real = np.transpose(x_real)
y_hat = np.matmul(x_real, m)+c    

    
error = 0.9*(np.sum((y-y_hat)**2))
print(error)

sum = np.sum(y_hat-y)
 
for epochs in range(10001):
    for items in range(n):
        m[items] = m[items] - (alpha*(sum*x[items]))
    c = c - (alpha*sum)
    y_hat = (np.matmul(x_real, m))+c
    error = 0.5*(np.sum((y-y_hat)**2))
    sum = np.sum(y_hat-y)
    
print(error)
plt.plot(x, y_hat)

x_real = []
x = np.array([math.log10(53)])
for i in range(1, n+1):
    x_real.append(x**i)
x_real = np.array(x_real)
x_real = np.transpose(x_real)
y_hat = np.matmul(x_real, m)+c
print(y_hat)
#end of this 
