import cv2
import os
import imutils
import numpy as np
import time

mode = list(map(int, input().split()))
path = "Model\\"

if mode[0] == 1: # tests data set
    path += "tests\\"
else: # training data set
    path += "training\\"

if mode[1] == 1: # Masks
    path += "masks"
elif mode[1] == 2: # Faces
    path += "faces"
else: # Random Negatives
    path += "negatives"

if os.path.exists(path) == False: # path does not already exist
    os.makedirs(path)

cap = cv2.VideoCapture(0)

saveCount = 0
while True:
    ret, frame = cap.read()
    key = cv2.waitKey(3)
    resizedImg = cv2.resize(frame, (200, 200)) 
    
    if key == ord('k'):
        currTime = time.time()
        cv2.imwrite(f"{path}/{saveCount}{currTime}.png", resizedImg)
        saveCount += 1

    cv2.imshow("Test", frame)

    if key == ord('q'):
        break 