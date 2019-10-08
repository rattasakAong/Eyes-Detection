import cv2

image = cv2.imread("two_people.jpg")
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eyes = eye_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

for (ex, ey, ew, eh) in eyes:
    cv2.rectangle(image, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

cv2.imshow("Eye Detected", image)

cv2.waitKey(0)
cv2.destroyAllWindows()