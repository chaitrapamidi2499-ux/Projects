# 👤 Face Recognition-Based Attendance System

## 📌 Project Overview

This project is a real-time **Face Recognition-Based Attendance System** developed using Python, OpenCV, dlib, and the `face_recognition` library. The application captures live video through a webcam, identifies registered individuals by comparing facial encodings, and automatically records attendance with the current date and time in a CSV file.

---

## 🎯 Problem Statement

Manual attendance systems are time-consuming, prone to human error, and require continuous supervision. This project aims to automate the attendance process using facial recognition technology, providing a faster, contactless, and more reliable solution.

---

## 📂 Dataset

The system uses a collection of registered face images stored locally.

Each image represents an authorized individual whose facial encoding is generated before real-time recognition.

Current registered users include:

- Chaitra
- Kanchana
- Srinivas
- Vamsi

---

## 🛠️ Technologies Used

- Python
- OpenCV
- dlib
- face_recognition
- NumPy
- CSV
- Webcam

---

## ⚙️ Project Workflow

1. Load images of registered individuals.
2. Generate facial encodings for each image.
3. Start live webcam feed.
4. Detect faces in each video frame.
5. Generate facial encodings for detected faces.
6. Compare detected encodings with stored encodings.
7. Identify recognized individuals.
8. Record attendance with the current date and time.
9. Prevent duplicate attendance entries for the same person on the same day.

---

## 🔍 Features

- Real-time face detection
- Face recognition using facial encodings
- Automatic attendance recording
- Date and time logging
- Duplicate attendance prevention
- CSV-based attendance storage
- Live webcam interface
- Unknown face detection

---

## 📊 Attendance Output

Attendance records are stored in:

```text
attendance.csv
```

Each entry contains:

- Name
- Date
- Time

---

## 💡 Key Highlights

- Uses the `face_recognition` library for accurate facial encoding and comparison.
- Automatically creates the attendance file if it does not already exist.
- Ensures that each person is marked only once per day.
- Performs face detection and recognition in real time using a webcam.
- Displays the recognized person's name on the video feed.

---

## 📁 Repository Structure

```text
Face Recognition-Based Attendance System/
│
├── FR.ipynb
├── attendance.csv
├── Images/
│   ├── Chaitra.jpg
│   ├── Kanchana.jpeg
│   ├── Srinivas.jpeg
│   └── Vamsi.jpeg
└── README.md
```

---

## 🚀 Future Improvements

- Integrate with a database instead of CSV.
- Develop a graphical user interface (GUI).
- Add user registration for new faces.
- Enable attendance reports and analytics.
- Support multiple cameras and larger face datasets.
- Deploy as a desktop or web application.

---

## 👩‍💻 Author

**Chaitra Pamidi**

Data Science | Machine Learning | Artificial Intelligence
