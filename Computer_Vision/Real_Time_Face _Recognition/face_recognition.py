"""
File: face_recognition
Name: Yu-Ju Fang
This file was adapted by Programming knowledge

In this file we load all the face data in the face_dataset file we collected by using face_data.py
and then combine the dataset and the label. Last, we open the webcam and detect all the faces in the
window and using KNN to classify which face is it and put the corresponding name next to the face on
window
"""
import numpy as np
import cv2
import os

# -----------------------------KNN CODE -------------------------------------
def distance(v1, v2):
    # Eucledian
    return np.sqrt(((v1 - v2) ** 2).sum())

def knn(train, test, k=5):
    dist = []

    for i in range(train.shape[0]):
        # Get vector and label
        ix = train[i, :-1]  # get the first data to the last second data on row i
        iy = train[i, -1]  # get the last data on row i

        # Compute the distance from test point
        d = distance(test, ix)
        dist.append([d, iy])

    # Sort based on distance and get top k
    dk = sorted(dist, key=lambda x: x[0])[:k]

    # Retrieve only the labels
    labels = np.array(dk)[:, -1]

    # Get frequencies of each label
    output = np.unique(labels, return_counts=True)
    # Find max frequency and corresponding label
    index = np.argmax(output[1])

    return output[0][index]
# -------------------------------------------------------------------------


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

dataset_path = './face_dataset/'
face_data = []  # store each face data
labels = []
class_id = 0  # Labels for every given file
names = {}  # mapping between id and name

# Dataset preparation: go through all the face_dataset file and load
# all the data we have collected by using face_data.py
for fx in os.listdir(dataset_path):
    if fx.endswith('.npy'):
        names[class_id] = fx[:-4]
        data_item = np.load(dataset_path + fx)
        face_data.append(data_item)

        target = class_id * np.ones((data_item.shape[0],))
        class_id += 1
        labels.append(target)

face_dataset = np.concatenate(face_data, axis=0)
face_labels = np.concatenate(labels, axis=0).reshape((-1, 1))
print(face_labels.shape)
print(face_dataset.shape)

trainset = np.concatenate((face_dataset, face_labels), axis=1)
print(trainset.shape)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    if ret == False:
        continue

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect multi faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for face in faces:
        x, y, w, h = face

        # Get the face ROI
        offset = 5
        faces_section = frame[y-offset:y+h+offset, x-offset:x+w+offset]
        faces_section = cv2.resize(faces_section, (100, 100))

        # Use KNN to classify which face is shown on the webcam
        out = knn(trainset, faces_section.flatten())

        # Put the name of the face in the original image
        cv2.putText(frame, names[int(out)], (x-35, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        # Draw rectangle in the original image
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Faces', frame)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()