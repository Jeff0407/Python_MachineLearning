"""
File: object_detection
Name;Yu-Ju Fang
This File was adapted from DeepLearning_by_PHDScholar's File and uses opensource on https://github.com/opencv/opencv
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
import time

frozen_model = 'frozen_inference_graph.pb'
config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'


def main():
    model = cv2.dnn_DetectionModel(frozen_model, config_file)
    classLabels = []
    file_name = 'Labels.txt'
    with open(file_name, 'rt') as fpt:
        classLabels = fpt.read().rstrip('\n').split('\n')

    model.setInputSize(320, 320)
    model.setInputScale(1.0 / 127.5)
    model.setInputMean((127.5, 127.5, 127.5))
    model.setInputSwapRB(True)

    cap = cv2.VideoCapture('road_trafifc.mp4')
    # cap = cv2.VideoCapture(1)

    # Check if the video is opend correctly
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError('Cannot open video')

    font_scale = 0.5
    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        ret, frame = cap.read()
        ClassIndex, confidence, bbox = model.detect(frame, confThreshold=0.55)
        if (len(ClassIndex) != 0):
            for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
                if (ClassInd <= 80):
                    cv2.rectangle(frame, boxes, (255, 0, 0), 2)
                    cv2.putText(frame, classLabels[ClassInd - 1], (boxes[0] + 10, boxes[1] + 40), font, thickness=2,
                                fontScale=font_scale, color=(0, 255, 0))
        cv2.imshow('Object Detection Turorial', frame)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()


