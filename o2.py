from scipy.misc import imread
import matplotlib.pyplot as plt
l = imread('d:/pyp/timg.jpg')
xmax=l.shape[0]
ymax=l.shape[1]
l[range(xmax),range(ymax)]=0
l[range(xmax-1,-1,-1),range(ymax)]=0
plt.imshow(l)
plt.show()
print(xmax)
print(ymax)