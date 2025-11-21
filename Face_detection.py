# Used in Mobile/laptop cameras

# openCV : used to process images and videos
# pip intsall opencv-python

import cv2

face_capture=cv2.CascadeClassifier("C:/Users/shubh/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml")


# It enables the use of the camera
vid_capture= cv2.VideoCapture(0)

# To keep the camera on, untill we press 'q'
while True:
    ret, video=vid_capture.read() # captures the video data
    color = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY) # converts the video data to grayscale
    faces = face_capture.detectMultiScale(
        color,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )


    for (x,y,w,h) in faces:
        cv2.rectangle(video, (x,y), (x+w, y+h), (0, 255, 0), 2)


    cv2.imshow("video_live",video) # displays the video data
    if cv2.waitKey(10) == ord('q'):
        break
vid_capture.release() # releases the camera


# how does it works:
# STEP 1: The camera is opened and it captures the video data.
# STEP 2: The video data is converted to gray color, making ut easier to dedect our face muscles
# STEP 3: The face muscles are detected using the haarcascade_frontalface_default.xml file.
# step 4 : The detected faces are drawn on the video data using rectangles.
# STEP 5: the captured data is colorized.


# NOTE: You can find your captured data in the fo;lder where you can installed CV2,
# C:\Users\shubh\AppData\Roaming\Python\Python312\site-packages\cv2\data

