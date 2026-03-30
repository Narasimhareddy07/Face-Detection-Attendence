import cv2
import face_recognition
import os
import mysql.connector

# ================= DATABASE CONNECTION =================
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Babblu@2727",
    database="face_attendance"
)

cursor = db.cursor()

# ================= LOAD DATASET =================
path = "dataset"
images = []
classNames = []

for file in os.listdir(path):
    img_path = os.path.join(path, file)
    img = face_recognition.load_image_file(img_path)
    images.append(img)
    classNames.append(os.path.splitext(file)[0])

print("Loaded Images:", classNames)

# ================= ENCODE FACES =================
def encode_faces(images):
    encodings = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_encodings(img)
        
        if len(faces) > 0:
            encodings.append(faces[0])
        else:
            print("⚠️ No face found in one image, skipping...")
    
    return encodings

known_encodings = encode_faces(images)

print("Encoding Completed!")

# ================= ATTENDANCE FUNCTION =================
marked_names = set()

def mark_attendance(name):
    if name not in marked_names:
        marked_names.add(name)
        query = "INSERT INTO attendance (name) VALUES (%s)"
        cursor.execute(query, (name,))
        db.commit()
        print(f"{name} marked present")

# ================= START CAMERA =================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not working")
    exit()

while True:
    success, frame = cap.read()

    # Resize frame (faster processing)
    small_frame = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_small)
    face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

    for encodeFace, faceLoc in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, encodeFace)
        name = "Unknown"

        if True in matches:
            matchIndex = matches.index(True)
            name = classNames[matchIndex]
            mark_attendance(name)

        # Scale coordinates back
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

        # Draw rectangle
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Put name text
        cv2.putText(frame, name, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Show output
    cv2.imshow("Face Attendance System", frame)

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break

# ================= CLEANUP =================
cap.release()
cv2.destroyAllWindows()
db.close()