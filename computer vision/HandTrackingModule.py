import cv2
import mediapipe as mp
import time

class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.6, trackingCon=0.6):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, 1, self.detectionCon, self.trackingCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipsIds = [4, 8, 12, 16, 20]
        
    def find_hands(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(image)
        
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
                
        return image
    
    def find_position(self, image, handNo=0):
        self.lmList = []
        
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            
            for id, lm in enumerate(myHand.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                
                cv2.circle(image, (cx, cy), 8, (255, 0, 255), -1)
        
        return self.lmList
    
    def fingers_up(self):
        fingers = []
        
        if len(self.lmList) > 0:
            # Thumb
            if self.lmList[self.tipsIds[0]][1] > self.lmList[self.tipsIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
                
            # Fingers
            for id in range(1, 5):
                if self.lmList[self.tipsIds[id]][2] < self.lmList[self.tipsIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                
        print(fingers)
        return sum(fingers)

cap = cv2.VideoCapture(0)
detector = HandDetector()

while True:
    _, frame = cap.read()
    image = detector.find_hands(frame)
    lmList = detector.find_position(image)
    fingersUp = detector.fingers_up()
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.putText(image, str(fingersUp), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
    cv2.imshow("Hands", image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
