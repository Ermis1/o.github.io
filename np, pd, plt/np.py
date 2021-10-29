from numpy import *
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a)
print(len(a))
print(type(a))
print(a[0])
print(a, b)
print(a+b)

print(np.size(a))
print(np.shape(a))
print(np.ndim(a))
print(np.sqrt(a))
print(a.itemsize)
print(a.dtype)
print(a.nbytes)

x = np.random.random(1)
print(x)

x = np.random.randint(1, 23)
print(x)

x = np.random.rand(1)
print(x)

x = np.random.randn(1)
print(x)

x = np.arange(1, 44, 9) #(1, 2), (1, 2, 0.5)
print(x)

x = np.random.permutation(np.arange(1, 10)) # (1, 2), (1, 2, 0.5)
print(x)

x = np.zeros((2, 4)) # (9), (2, 3, 4)
print(x)

x = np.ones(2)
print(x)

c = np.array([(1, 2, 3), (1, 2, 3)])

print(np.min(c))
print(np.min(c, axis=0))
print(np.max(c))
print(np.max(c, axis=1))
print(np.sum(c))
print(np.sum(c, axis=0))
print(np.std(c))
print(np.std(c, axis=1))
print(np.mean(c))
print(np.mean(c, axis=0))
print(np.median(c))
print(np.median(c, axis=1))