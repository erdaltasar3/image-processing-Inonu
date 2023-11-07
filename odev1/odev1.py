import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:/Users/erdal/OneDrive/Belgeler/image-processing/images/ucak.jpg",0)

def calculate_histogram(image):
    histogram = np.zeros((256,), dtype=int)
    height, width = image.shape

    for i in range(height):
        for j in range(width):
            pixel_value = image[i, j]
            histogram[pixel_value] += 1

    return histogram

histogram = calculate_histogram(img)

plt.plot(histogram)
plt.title('Gri Resim Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.show()


cv2.waitKey()
cv2.destroyAllWindows()
