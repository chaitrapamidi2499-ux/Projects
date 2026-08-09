# 🫁 Pneumonia Detection Using CNN

> A deep learning-based image classification system that analyzes chest X-ray images and detects whether they are **NORMAL** or **PNEUMONIA** using a VGG19-based Convolutional Neural Network.

---

# 📌 Overview

The **Pneumonia Detection Using CNN** project is a deep learning-based image classification system developed to detect pneumonia from chest X-ray images. The project uses **VGG19 transfer learning** with ImageNet pretrained weights to extract visual features from chest X-ray images and classify them into Normal and Pneumonia categories.

The project includes image preprocessing, model training, performance evaluation, and a Flask-based application that allows users to upload a chest X-ray image and receive a prediction.

---

# 📸 Project Preview

<img width="1917" height="1010" alt="Upload" src="https://github.com/user-attachments/assets/368776b0-556a-4c20-868e-843ab5a3c26c" />
<img width="1917" height="1002" alt="Predict_1" src="https://github.com/user-attachments/assets/a45ce325-4c66-4002-ab4e-47d766f2335c" />
<img width="1917" height="1012" alt="Predict_2" src="https://github.com/user-attachments/assets/4d8f937c-61a1-4e74-9286-3232aee06d9d" />

---

# 🎯 Objectives

- Detect pneumonia from chest X-ray images.
- Classify chest X-rays into Normal and Pneumonia categories.
- Apply transfer learning using the VGG19 architecture.
- Preprocess chest X-ray images for deep learning.
- Evaluate model performance using classification metrics.
- Build a Flask application for image-based pneumonia prediction.

---

# ✨ Features

- VGG19 Transfer Learning
- Chest X-ray Image Classification
- Image Preprocessing
- Binary Classification
- Model Training and Evaluation
- Classification Report
- Confusion Matrix Analysis
- ROC Curve Analysis
- Flask-based Prediction Application
- Image Upload and Prediction

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Deep Learning | TensorFlow, Keras |
| Model | VGG19 |
| Image Processing | OpenCV, PIL, scikit-image |
| Data Analysis | NumPy, Pandas |
| Visualization | Matplotlib, Seaborn |
| Model Evaluation | Scikit-learn |
| Deployment | Flask |

---

# 📂 Project Structure

    Pneumonia-Detection-Using-CNN/
    │
    ├── pneumonia_detection_cnn.ipynb
    ├── app.py
    ├── model.keras
    │
    ├── templates/
    │   └── index.html
    │
    ├── static/
    │   └── ...
    │
    ├── uploads/
    │   └── ...
    │
    └── README.md

---

# 📊 Model Performance

The project uses a **VGG19-based transfer learning model** trained to classify chest X-ray images into **NORMAL** and **PNEUMONIA** classes.

## Model Configuration

| Parameter | Value |
|-----------|-------|
| Architecture | VGG19 |
| Pretrained Weights | ImageNet |
| Input Size | 128 × 128 × 3 |
| Output Classes | 2 |
| Optimizer | SGD |
| Learning Rate | 0.0001 |
| Momentum | 0.1 |
| Nesterov | True |
| Loss Function | Categorical Cross-Entropy |
| Dropout | 0.2 |
| Training Epochs | 10 |

## Evaluation Results

| Metric | Score |
|--------|-------|
| Validation Accuracy | **68.75%** |
| Validation Loss | **0.5119** |
| Test Accuracy | **77.56%** |
| Test Loss | **0.4499** |

## Classification Report

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| NORMAL | **0.93** | **0.44** | **0.59** |
| PNEUMONIA | **0.74** | **0.98** | **0.85** |
| **Overall Accuracy** | | | **0.78** |

The model achieved a **77.56% test accuracy** on the test dataset.

The model demonstrated particularly strong recall for the **PNEUMONIA** class, achieving **98% recall**, while the **NORMAL** class achieved **44% recall**.

---

# 🔄 Project Workflow

    Chest X-Ray Dataset
            │
            ▼
    Data Preparation
            │
            ▼
    Image Preprocessing
            │
            ▼
    Image Resizing
            │
            ▼
    VGG19 Feature Extraction
            │
            ▼
    Custom Classification Layers
            │
            ▼
    Model Training
            │
            ▼
    Model Evaluation
            │
            ▼
    Flask Application
            │
            ▼
    NORMAL / PNEUMONIA

---

# 🔍 Key Insights

The model evaluation provides the following insights:

- The model achieved a **77.56% test accuracy**.
- The model achieved a **98% recall for Pneumonia**.
- Pneumonia classification achieved an **F1-score of 0.85**.
- Normal classification achieved a **93% precision**.
- Normal-class recall was **44%**.
- The model was more effective at identifying Pneumonia cases than Normal cases.
- The difference between training and validation performance indicates opportunities to improve model generalization.
- Improving Normal-class recall would be an important area for future development.

---

# 📸 Model Evaluation

The project evaluates the trained model using multiple performance metrics and visualizations.

## Classification Report

The classification report evaluates the model based on:

- Precision
- Recall
- F1-Score
- Support
- Overall Accuracy

---

# 🌐 Flask Application

The trained model is integrated into a **Flask web application** that allows users to upload a chest X-ray image and receive a prediction.

## Prediction Workflow

    User Uploads X-Ray
            │
            ▼
    Flask Application
            │
            ▼
    Image Preprocessing
            │
            ▼
    Resize to 128 × 128
            │
            ▼
    VGG19 Model
            │
            ▼
    Model Prediction
            │
            ▼
    NORMAL / PNEUMONIA

---

# 🚀 Future Improvements

- Improve model accuracy through hyperparameter tuning.
- Experiment with other CNN architectures.
- Fine-tune VGG19 layers for better feature extraction.
- Apply advanced image augmentation techniques.
- Improve Normal-class classification performance.
- Address potential class imbalance.
- Experiment with higher-resolution X-ray images.
- Add prediction confidence scores.
- Improve the Flask application interface.
- Deploy the application to a cloud platform.

---

# 📚 Learning Outcomes

Through this project, I gained hands-on experience in:

- Convolutional Neural Networks
- Transfer Learning
- VGG19 Architecture
- Medical Image Classification
- TensorFlow and Keras
- Image Preprocessing
- Deep Learning Model Training
- Model Evaluation
- Classification Metrics
- Confusion Matrix Analysis
- ROC Curve Analysis
- Flask Model Deployment
- Deep Learning Application Development

---

---

# 👩‍💻 Author

**Chaitra Pamidi**  
*Data Analytics • Data Science • Machine Learning • Artificial Intelligence*

---

⭐ **If you found this project interesting, feel free to explore the repository and connect with me!**
