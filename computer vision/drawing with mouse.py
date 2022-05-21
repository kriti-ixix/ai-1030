# Importing the libraries
import cv2
import numpy as np

# Events available
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# Function to draw a circle
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(blank, (x, y), 50, (204, 153, 255), -1)
        
# Create a blank image
blank = np.zeros((500, 500, 3), np.uint8)
cv2.namedWindow(winname="My Drawing")

# Setting a mouse callback
cv2.setMouseCallback("My Drawing", draw_circle)

# Displaying the window
while True:
    cv2.imshow("My Drawing", blank)
    
    if cv2.waitKey(1) & 0xFF == 27: # If ESC key is pressed
        break
        
# Closing the window
cv2.destroyAllWindows()