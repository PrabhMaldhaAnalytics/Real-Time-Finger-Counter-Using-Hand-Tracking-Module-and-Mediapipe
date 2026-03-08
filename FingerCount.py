import cv2
from cvzone.HandTrackingModule import HandDetector


cap=cv2.VideoCapture(0)
cap.set(3,650)
cap.set(4,650)

detector=HandDetector(detectionCon=0.7,maxHands=2)


while True :
    success,img=cap.read()
    if not success:
        print("Failed to read from camera.")
        break
    
    hands,img=detector.findHands(img)
    

    if hands:
        for i ,hand in enumerate(hands) :
            fingers=detector.fingersUp(hand)
            count=fingers.count(1)
            handType=hand["type"]

            cv2.putText(img,f'{handType} Hand : {count}',
                    (10 , 100 + i*50),
                    cv2.FONT_HERSHEY_PLAIN , 1.2 , (255, 0 , 0) ,3)

    
    
    cv2.imshow('Fingers_count', img)
    if cv2.waitKey(1) & 0xFF==ord('q') :
        break

cap.release()
cv2.destroyAllWindows()    