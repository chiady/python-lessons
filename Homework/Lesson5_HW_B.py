import opencv as cv2
import matplotlib.pyplot as plt

img = cv2.imread('xxxxx.tif', cv2.IMREAD_UNCHANGED)
print(type(img), img.shape, img.dtype)

plt.imshow(img, cmap='gray')
plt.show()