import cv2 
import mediapipe as mp 
import pyautogui


x1 = y1 = x2 = y2 = 0
cam = cv2.VideoCapture(0)



if not cam.isOpened():
    print('Cannot detect webcam')
    
    
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

    
while True:
    ret , frame = cam.read()
    
    frame_height ,frame_width , _ = frame.shape
    frame = cv2.flip(frame , 1)
    
    if not ret:
        print('Cant detect frames')
        
    
    rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb)
    
    hands = output.multi_hand_landmarks
    
    
    
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            
            for id , landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 8:
                    cv2.circle(img=frame , center=(x,y) , radius=8 , color= (0,255,255) , thickness=3)
                    x1 = x 
                    y1 = y
                if id == 4:
                    cv2.circle(img=frame , center=(x,y) , radius=8 , color= (0,0,255) , thickness=3)
                    x2 = x 
                    y2 = y
                    dist = ((x2-x1)**2 + (y2-y1)**2)*(0.5)//4
                    cv2.line(frame , (x1 , y1) , (x2, y2) , (255,255,255) , 3)
                    
                    
                    if dist > 50:
                        pyautogui.press('Volumeup')
                    else:
                        pyautogui.press('Volumedown')
    cv2.imshow('Webcam Activated' , frame)  
    
    key = cv2.waitKey(10)
    
    if key == 27:
        break 
    
cam.release()
cv2.destroyAllWindows()