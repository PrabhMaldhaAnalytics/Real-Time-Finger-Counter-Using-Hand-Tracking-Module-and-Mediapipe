import cv2
import mediapipe as mp

mp_hands= mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap=cv2.VideoCapture(0)

winwidth = 600
winheight = 600

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():#Loading and processing the video
           ret, frame = cap.read()
           if not ret:
              break

           rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # convert the background from bgr to rgb
           process_frames = hands.process(rgb_frame)

           if process_frames.multi_hand_landmarks: #Draw landmarks on the frame
                 for lm in process_frames.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)
                     
                  
                 
           resized_frame = cv2.resize(frame, (winwidth, winheight))#resize the frame to the desired window size

           cv2.imshow('Hand Tracking', resized_frame) #Display the resized frame

           if cv2.waitKey(1) & 0xFF==ord('q') :
             break

cap.release()
cv2.destroyAllWindows()    
