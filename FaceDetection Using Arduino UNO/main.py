import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
detector = FaceDetector()
arduino = SerialObject()
while True:
    success, img = cap.read()

    img, bBoxes = detector.findFaces(img)
    
    if bBoxes:
        arduino.sendData([1,0]) //green
    else:
        arduino.sendData([0,1])  //red  

    cv2.imshow("Video",img)
    cv2.waitKey(1)