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
            print(self.results.multi_hand_landmarks)
            for handLms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
                
        return image
    
    
cap = cv2.VideoCapture(0)
detector = HandDetector()

while True:
    _, frame = cap.read()
    image = detector.find_hands(frame)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    cv2.imshow("Hands", image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()