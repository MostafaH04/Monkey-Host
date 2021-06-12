import cv2
import tensorflow as tf
import numpy as np
import os
from PIL import Image
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model('ModelFile')

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    key = cv2.waitKey(1)    

    newframe = cv2.resize(frame, (200, 200))
    cv2.imwrite("1.png", newframe)
    predictImg = image.load_img("1.png", target_size= (200,200))
    predictImgArr = image.img_to_array(predictImg)
    predictImgArr = np.expand_dims(predictImgArr, axis = 0)
    
    predictionImg = np.vstack([predictImgArr])
    
    prediction = model.predict(predictionImg, batch_size = 10)
    if int(prediction[0][0]) == 0:
        print("Person")
        


    os.remove('1.png')

    if key == ord('q'):
        break




