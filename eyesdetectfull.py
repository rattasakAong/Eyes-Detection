import numpy as np
import cv2

cap = cv2.VideoCapture(0)

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    eyes = eye_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
    for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(frame, (ex,ey), (ex + ew , ey + eh), (255, 0, 0), 3)

    cv2.imshow("Eye Detected", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()