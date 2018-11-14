from scipy.misc import imread 
import matplotlib.pyplot as plt
lena = imread('d:/pyp/timg.jpg')
acopy = lena.copy()
aview = lena.view()
lena.flat=210
plt.subplot(221)
plt.imshow(lena)
acopy.flat=30
plt.subplot(222)
plt.imshow(acopy)
aview.flat=200
plt.subplot(223)
plt.imshow(aview)
aview.flat=300
plt.subplot(224)
plt.imshow(aview)
plt.show()
