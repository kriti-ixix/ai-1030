import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

# Capturing the background
time.sleep(3)
background = 0

for i in range(10):
    ret, background = cap.read()
    
background = np.flip(background, axis = 1)

# Main loop
while cap.isOpened():
    # Reading and flipping the image
    ret, image = cap.read()
    image = np.flip(image, axis = 1)
    
    # Converting to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    blurred = cv2.GaussianBlur(hsv, (35, 35), 0)
    
    # Defining a red range for first mask
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    
    # Defining a red range for second mask
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    
    # Adding the final mask 
    mask = mask1 + mask2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    
    # Replace the mask with the background
    image[np.where(mask==255)] = background[np.where(mask==255)]

    cv2.imshow('Invisibility Cloak', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()