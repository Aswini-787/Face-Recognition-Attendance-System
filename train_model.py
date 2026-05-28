import os
import cv2
import face_recognition
import pickle

dataset_dir = "dataset"

known_encodings = []
known_names = []

for person_name in os.listdir(dataset_dir):

    person_folder = os.path.join(dataset_dir, person_name)

    if not os.path.isdir(person_folder):
        continue

    for image_name in os.listdir(person_folder):

        image_path = os.path.join(person_folder, image_name)

        image = cv2.imread(image_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(person_name)

data = {
    "encodings": known_encodings,
    "names": known_names
}

os.makedirs("encodings", exist_ok=True)

with open("encodings/encodings.pickle", "wb") as f:
    f.write(pickle.dumps(data))

print("Training completed!")