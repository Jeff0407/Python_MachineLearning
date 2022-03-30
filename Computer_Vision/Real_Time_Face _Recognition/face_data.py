"""
File: face_data
Name: Yu-Ju Fang
This file was adapted by Programming knowledge

The function of this file is we open our webcam to collect the face data of our own face or faces you want to
recognize and save it in a file called face_dataset
Use haarcascade classifier which detects the edge of the whole image to find out where the face is
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

skip = 0
face_data = []  # store each face data
dataset_path = './face_dataset/'
file_name = input('Enter the name of person: ')

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret == False:
        continue

    # Find the upper left, upper right, lower left and lower right coordinate of your face
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)  # frame_name, scaling factor, number of neighbors

    if len(faces) == 0:
        continue

    k = 1

    faces = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)  # Sort the faces by area in descending order
    skip += 1
    for face in faces[:1]:
        x, y, w, h = face
        offset = 5  # padding
        face_offset = frame[y-offset: y+h+offset, x-offset:x+w+offset]
        face_selection = cv2.resize(face_offset, (100, 100))
        if skip % 10 == 0:
            face_data.append(face_selection)
            print(len(face_data))
        k += 1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("face", frame)

    if cv2.waitKey(1) == ord('q'):
        break

face_data = np.array(face_data)
face_data = face_data.reshape((face_data.shape[0], -1))
np.save(dataset_path + file_name, face_data)
print("Dataset saved at: {}". format(dataset_path + file_name + '.npy'))

cap.release()
cv2.destroyAllWindows()