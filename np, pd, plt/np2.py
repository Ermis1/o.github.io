from numpy import *
import numpy as np

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])

print(a)
print(len(a))
print(type(a))
print(a[0])
print(a, b)
print(a + b)

print(np.size(a))
print(np.shape(a))
print(np.ndim(a))
print(a.dtype)
print(a.itemsize)
print(a.nbytes)
print(np.sqrt(a))

x = np.random.random(1)
print(x)

x = np.random.randint(0, 10)
print(x)

x = np.random.rand(1)
print(x)

x = np.random.randn(1)
print(x)

x = np.arange(0, 10, 2)
print(x)

x = np.random.permutation(np.arange(0, 10))
print(x)

x = np.zeros((3, 3)) # ((3, 3, 2))
print(x)       

x = np.ones(4)
print(x)      

x[0] = 2
print(x)


c = np.array([(2, 3, 4), (5, 6, 7)])

print(np.min(c))
print(np.min(c, axis=0))
print(np.max(c))
print(np.max(c, axis=1))
print(np.sum(c))
print(np.sum(c, axis=0))
print(np.mean(c))
print(np.mean(c, axis=1))
print(np.median(c))
print(np.median(c, axis=0))
print(np.std(c))
print(np.std(c, axis=1))
print(np.prod(c))
print(np.prod(c, axis=0))