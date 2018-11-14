import numpy as np
data=np.loadtxt("d:/pyp/t.csv",delimiter=",",skiprows=1)
print(data)
(a, b) = np.loadtxt("d:/pyp/t.csv", dtype=int, skiprows=1, comments='#', delimiter=",", usecols=(0, 2), unpack=True)
print(a,b)
def add_one(x):
    return int(x)+1
(a, b) = np.loadtxt("d:/pyp/t.csv", dtype=int, skiprows=1, converters={2:add_one}, comments='#', delimiter=',', usecols=(0, 2), unpack=True)
print(a, b)