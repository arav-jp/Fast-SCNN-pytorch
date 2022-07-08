import cv2

cap = cv2.VideoCapture(2)
ret, frame = cap.read()
cv2.imwrite("/home/arav/buffalo/repos/Fast-SCNN-pytorch/png/capture.png", frame)