import cv2
import time
import handlandmarkmodule as hnd
pTime = 0
cTime = 0
webcame = cv2.VideoCapture(0)
#initialize the object
detector = hnd.handDetector()
while webcame.isOpened():
     success, imgbgr = webcame.read()
     
     #resizing the frame for better view
     imgbgr = cv2.resize(imgbgr, (1000,700))
     
     imgbgr = detector.findHands(imgbgr, draw = True)
     lmList = detector.findPosition(imgbgr, draw=False)
     if len(lmList) != 0:
        print(lmList[4])#you can use any id other than 4
     cTime = time.time()
     fps = 1 / (cTime - pTime)
     pTime = cTime
 
    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
     #           (255, 0, 255), 3)
 
     cv2.imshow("Image", imgbgr)   
     key = cv2.waitKey(1)
     if (key == 81) or (key == 113):
          break
webcame.release()
cv2.destroyAllWindows()