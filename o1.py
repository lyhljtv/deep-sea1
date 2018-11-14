import numpy as np
b = np.arange(10).reshape(2,5)
print("In: b")
print(b)
print(b.ndim)
print(b.T)
print(b.itemsize)
m=b.flat
for item in m: 
	print(item)