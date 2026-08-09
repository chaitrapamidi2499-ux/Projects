# 😊 Face Recognition-Based Attendance System

> An AI-powered attendance management system that uses facial recognition to automatically identify individuals through a webcam and record their attendance in real time.

---

# 📌 Overview

The **Face Recognition-Based Attendance System** is a computer vision application that automates attendance tracking using facial recognition technology. Instead of manually recording attendance, the system identifies registered individuals through a webcam, matches their facial features with stored face encodings, and logs attendance with the current date and time.

The project demonstrates the practical application of Computer Vision and Artificial Intelligence for automating repetitive tasks while improving accuracy and efficiency.

---

# 📸 Project Preview

<img width="1920" height="1080" alt="FR" src="https://github.com/user-attachments/assets/a98d46ae-1d63-4794-bbfc-3e628161fa62" />

---

# 🎯 Objectives

- Automate attendance marking using facial recognition.
- Detect and recognize multiple registered individuals in real time.
- Eliminate duplicate attendance entries for the same day.
- Store attendance records in a structured CSV file.
- Demonstrate real-time computer vision using Python.

---

# ✨ Features

- Real-time face detection using webcam
- Facial recognition using face encodings
- Automatic attendance logging
- Duplicate attendance prevention
- Date and time stamping
- Unknown face detection
- CSV-based attendance storage

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Computer Vision | OpenCV |
| Face Recognition | face_recognition, dlib |
| Numerical Computing | NumPy |
| Data Storage | CSV |
| Environment | Jupyter Notebook |

---

# 📂 Project Structure

```text
Face-Recognition-Based-Attendance-System/
│
├── face_recognition_system.ipynb
├── Images/
│   ├── Chaitra.jpg
│   ├── Kanchana.jpeg
│   ├── Srinivas.jpeg
│   └── Vamsi.jpeg
├── attendance.csv
├── images/
└── README.md
```

---

# 🔄 Project Workflow

```text
Register Known Faces
          │
          ▼
Generate Face Encodings
          │
          ▼
Start Webcam
          │
          ▼
Detect Faces
          │
          ▼
Extract Face Encodings
          │
          ▼
Compare with Registered Faces
          │
          ▼
Recognize Person
          │
          ▼
Mark Attendance
          │
          ▼
Save to CSV
```

---

# 🤖 System Workflow

The application performs the following tasks:

- Loads images of registered individuals.
- Generates facial encodings for each registered face.
- Captures live video from the webcam.
- Detects faces in each video frame.
- Extracts facial embeddings from detected faces.
- Compares live face encodings with registered encodings.
- Identifies matching individuals.
- Marks attendance with the current date and time.
- Prevents duplicate attendance entries on the same day.

---

# 📊 Attendance Record

Attendance is automatically stored in a CSV file with the following information:

| Name | Date | Time |
|------|------|------|
| Person Name | DD-MM-YYYY | HH:MM:SS |

Each individual is recorded only once per day.

---

# 🔍 Key Highlights

- Real-time face recognition using a webcam.
- Face matching based on facial encoding similarity.
- Automatic attendance logging without manual intervention.
- Unknown individuals are identified and not recorded.
- Prevents duplicate attendance entries for the same date.
- Lightweight implementation using Python and OpenCV.

---

# 🚀 Future Improvements

- Integrate a database instead of CSV storage.
- Support multiple face registrations through the application.
- Develop a graphical user interface (GUI).
- Enable cloud-based attendance management.
- Add email notifications and attendance reports.
- Improve recognition performance under varying lighting conditions.

---

# 📚 Learning Outcomes

Through this project, I gained hands-on experience in:

- Computer Vision using OpenCV
- Facial Recognition using the `face_recognition` library
- Real-time webcam processing
- Face encoding and comparison techniques
- Attendance automation
- CSV file handling in Python
- Building AI-powered desktop applications

---

# 👩‍💻 Author

**Chaitra Pamidi**  
*Data Analytics • Data Science • Machine Learning • Artificial Intelligence*

---

⭐ **If you found this project interesting, feel free to explore the repository and connect with me!**
