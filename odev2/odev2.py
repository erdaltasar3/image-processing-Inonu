import cv2
import numpy as np

cam = cv2.VideoCapture(0)

cv2.namedWindow("frame")

def nothing(x):
    pass

cv2.createTrackbar("H1", "frame", 0 , 359, nothing)
cv2.createTrackbar("H2", "frame", 0 , 359, nothing)
cv2.createTrackbar("S1", "frame", 0 , 255, nothing)
cv2.createTrackbar("S2", "frame", 0 , 255, nothing)
cv2.createTrackbar("V1", "frame", 0 , 255, nothing)
cv2.createTrackbar("V2", "frame", 0 , 255, nothing)


while cam.isOpened():
    
    ret, frame = cam.read()
    
    H1 = int(cv2.getTrackbarPos("H1", "frame"))
    H2 = int(cv2.getTrackbarPos("H2", "frame"))
    S1 = cv2.getTrackbarPos("S1", "frame")
    S2 = cv2.getTrackbarPos("S2", "frame")
    V1 = cv2.getTrackbarPos("V1", "frame")
    V2 = cv2.getTrackbarPos("V2", "frame")
    
    if not ret:
        print("Video bitti veya kapatildi")
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) burada kırmızı ve mavi yer değişir
    
    #lower = np.array([110,50,50])
    #upper = np.array([130,255,255])
    
    lower = np.array([H1,S1,V1])
    upper = np.array([H2,S2,V2])

    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
        
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("video kapandi")
        break
    
    
cv2.destroyAllWindows()