import cv2
import numpy as np

# Resim okuma islemi 

img = cv2.imread("C:/Users/erdal/OneDrive/Belgeler/image-processing/images/rice2.jpg")

# Resim buyuk oldugu icin boyut ayarlama islemi 

cv2.namedWindow("original image",cv2.WINDOW_NORMAL)
cv2.namedWindow("mask1", cv2.WINDOW_NORMAL)
cv2.namedWindow("mask1_copy", cv2.WINDOW_NORMAL)

# Resmi gri tona cevirme islemi

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# treshold islemi
_, mask = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY) # 100 pikselin uzerindekileri 255 yap

# Morfolojik işlemler
iyilestirme_boyutu = np.ones((5, 5), np.uint8)
mask1 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, iyilestirme_boyutu, iterations=2)

mask1_copy = cv2.morphologyEx(mask, cv2.MORPH_OPEN, iyilestirme_boyutu, iterations=2)


# Sınırları bulma islemi
contours, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Pirinç sayısı
pirinc_Sayisi = len(contours)

# Her bir pirince benzersiz bir etiket ata
for i, contour in enumerate(contours, 1):
    cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.putText(img, f"{i}", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2)


# Konturları bul
contours, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Pirinç sayısı
rice_count = len(contours)

# Her bir pirince benzersiz bir etiket ata
for i, contour in enumerate(contours, 1):
    cv2.drawContours(mask1, [contour], -1, (0, 255, 0), 2)
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.putText(mask1, f"{i}", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 8)






cv2.imshow("original image",img)
cv2.imshow("mask1", mask1)
cv2.imshow("mask1_copy", mask1_copy)

cv2.waitKey()
cv2.destroyAllWindows()