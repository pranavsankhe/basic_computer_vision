import cv2 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm 
import numpy as np 


def plot(img):
	x_len = len(img[0])
	y_len = len(img)

	X = [i for i in range(x_len)]
	Y = [i for i in range(y_len)]

	fig = plt.figure()
	ax = fig.add_subplot(111, projection = '3d')
	z = np.array(img)
	x,y = np.meshgrid(X, Y)
	ax.plot_surface(x,y,z, linewidth = 0, cstride = 20, rstride = 20, cmap = cm.hot)
	plt.show()

img = cv2.imread('/Users/pranavsankhe/Pictures/UNADJUSTEDNONRAW_thumb_106f.jpg', 0)
# cv2.imshow('test_image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plot(img)


