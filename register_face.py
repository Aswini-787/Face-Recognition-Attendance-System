import cv2
import os

import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input("Enter student name: ")

dataset_dir = "dataset"
student_dir = os.path.join(dataset_dir, name)

# Create folders if they don't exist
os.makedirs(student_dir, exist_ok=True)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1

        face = frame[y:y+h, x:x+w]

        file_path = os.path.join(student_dir, f"{count}.jpg")
        cv2.imwrite(file_path, face)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow("Register Face", frame)

    if count >= 20:
        break

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

print("Images saved in:", student_dir)
