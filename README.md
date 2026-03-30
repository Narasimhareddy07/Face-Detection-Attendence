🧠 Face Detection Attendance System

An intelligent attendance management system that uses **computer vision** to automatically detect and recognize faces in real time and mark attendance. This system reduces manual effort and improves accuracy using AI-based recognition.

---

## 🚀 Features

* 👤 Real-time face detection using OpenCV
* 🧠 Face recognition-based identification
* 🧾 Automatic attendance marking
* 🗄️ Stores attendance data in MySQL database
* 📊 Easy tracking of attendance records
* ⚡ Fast and efficient system

---

## 🛠️ Technologies Used

* Python
* OpenCV
* NumPy
* MySQL
* Tkinter / Flask (for UI, if used)

---

## ⚙️ How It Works

1. Capture images of users and store them in the dataset
2. Train the model using facial data
3. Use webcam to detect faces in real time
4. Recognize the person using trained model
5. Mark attendance with date and time in database

---

## 📂 Project Structure

```
Face-Attendance-System/
│── dataset/              # Stored face images  
│── trainer/              # Trained model files  
│── attendance/           # Attendance records  
│── main.py               # Main program  
│── database.sql          # MySQL database setup  
│── README.md             # Project documentation  
```

---

## ▶️ Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/your-username/face-attendance-system.git
cd face-attendance-system
```

### 2. Install Dependencies

```
pip install opencv-python numpy mysql-connector-python
```

### 3. Setup Database

* Open MySQL
* Create database
* Import `database.sql` file

### 4. Run the Project

```
python main.py
```

---

## 📸 Output (Add Screenshots Here)

* Face detection window
* Attendance marked in database

---

## 📌 Use Cases

* Colleges & Universities
* Offices & Organizations
* Smart classroom systems

---

## ⚠️ Limitations

* Requires good lighting conditions
* Accuracy depends on dataset quality

---

## 🚀 Future Enhancements

* Mask detection support
* Cloud database integration
* Mobile app support
* Advanced deep learning models

---

## 👨‍💻 Author

**Narasimha Reddy**
🔗 GitHub: https://github.com/Narasimhareddy07

---

## 📄 License

This project is licensed under the MIT License.
