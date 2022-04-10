# -*- coding: utf-8 -*-
"""Implement from scratch a sampling method to draw samples from a multivariate Normal (MVN) distribution in JAX..ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10c51SgpvfIwmT6vXok0A-Ej13z24Qurp
"""

import numpy as np 
import jax.numpy as jnp 
import jax

import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# Define dimension. 
d = 2

# Set mean vector. 
m = jnp.array([1, 2]).reshape(2, 1)

# Set covariance function. 
K_0 = jnp.array([[2, 1],
                [1, 2]])

np.linalg.eigvals(K_0)

# Define epsilon.
epsilon = 0.0001

# Add small pertturbation. 
K = K_0 + epsilon*jnp.identity(d)

#  Cholesky decomposition.
L = jnp.linalg.cholesky(K)
L

jnp.dot(L, np.transpose(L))

"""alternative of jax.random.normal"""

import math
x = 20
ls = []
for i in range(x):
    a = np.random.randint(1,100)
    ls.append(a)

m = np.mean(ls) 

s = np.std(ls)
u1=[]
def gaussian(ls,m,s):
    for i in ls:
        y = (1 / (s * (math.sqrt(2 * math.pi)))) * math.exp((-1/2) * math.pow(((i-m)/s),2))
        
        u1.append(y)
    return u1   
gaussian(ls,m,s)    
u2=np.array(u1)
u = np.reshape(u2,(2,10))
print(u)

x = m + np.dot(L, u)

sns.jointplot(x=x[0], y=x[1], kind="kde", space=0);

z_1 = np.random.normal(loc=0, scale=1, size=n)
z = np.random.normal(loc=0, scale=1, size=n)
z_2 = np.sign(z)*z_1
sns.jointplot(x=z_1, y=z_2, kind="kde", space=0);