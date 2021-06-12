import cv2
import tensorflow as tf
import numpy as np
import os
from PIL import Image
from tensorflow.keras.preprocessing import image
import time
import glob

model = tf.keras.models.load_model('ModelFile')

cap = cv2.VideoCapture(0)

imgArr = []
size = (200,200)

def startSearch():
    global imgArr
    global size
    countPers = 0
    currTime = time.time()
    startingTime = currTime
    try:
        os.remove("1.png")
    except:
        print("1.png does not exists, proceeding on")
    while True:
        success, frame = cap.read()
        key = cv2.waitKey(1) 
        imgArr.append(frame)
        height, width = frame.shape[:2]
        size = (width, height)

        newframe = cv2.resize(frame, (200, 200))
        cv2.imwrite(f"{1}.png", newframe)
        predictImg = image.load_img(f"{1}.png", target_size= (200,200))
        predictImgArr = image.img_to_array(predictImg)
        predictImgArr = np.expand_dims(predictImgArr, axis = 0)
        
        predictionImg = np.vstack([predictImgArr])
        
        prediction = model.predict(predictionImg, batch_size = 10)
        if int(prediction[0][0]) == 0:
            countPers += 1
            currTime = time.time()

        if time.time() - currTime > 5:
            countPers = 0

        if countPers > 5:
            return True
        
        if time.time() - startingTime > 1200:
            return False

        os.remove("1.png")

        if key == ord('q'): 
            break
    os.remove("1.png")
    return False

path = "vidsout\\"
def vidOut(filename):
    global path
    global size
    #fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    path+= f"{filename}.avi"
    if os.path.exists(path):
        return "Path already exists"
    
    imgOutput = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

    for frameNum in range(len(imgArr)):
        imgOutput.write(imgArr[frameNum])
    imgOutput.release()
    return "Done, check the video file"