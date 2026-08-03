# 🩻 Pneumonia Detection from Chest X-rays using Deep Learning (VGG19)

## 📌 Project Overview

Pneumonia is a serious lung infection that can be life-threatening if not diagnosed and treated early. Chest X-ray imaging is one of the most widely used diagnostic methods for detecting pneumonia. This project develops a deep learning model capable of automatically classifying chest X-ray images as **Pneumonia** or **Normal** using Transfer Learning with the VGG19 architecture.

The project covers the complete deep learning workflow, including data preprocessing, image augmentation, model development, training, evaluation, model saving, and deployment through a Flask web application for real-time predictions.

---

## 🎯 Problem Statement

Manual examination of chest X-ray images requires experienced radiologists and can be time-consuming, especially in regions with limited healthcare resources.

The objective of this project is to develop an automated image classification system that assists in detecting pneumonia from chest X-ray images using Convolutional Neural Networks (CNNs).

---

## 🎯 Objectives

- Build an automated pneumonia detection system.
- Apply Transfer Learning using the VGG19 architecture.
- Improve model generalization through image augmentation.
- Compare predicted labels with actual chest X-ray images.
- Save the trained model for future inference.
- Deploy the model using Flask for user-friendly image prediction.

---

## 📂 Dataset

**Dataset:** Chest X-ray Images (Pneumonia)

The dataset contains chest X-ray images divided into two classes:

- NORMAL
- PNEUMONIA

### Dataset Structure

```text
chest_xray/
│
├── train/
│   ├── NORMAL/
│   └── PNEUMONIA/
│
├── val/
│   ├── NORMAL/
│   └── PNEUMONIA/
│
└── test/
    ├── NORMAL/
    └── PNEUMONIA/
```

The dataset is organized into separate training, validation, and testing folders to support model development and evaluation.

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- OpenCV
- NumPy
- Matplotlib
- Scikit-image
- Flask
- HTML
- CSS

---

## ⚙️ Project Workflow

1. Load the chest X-ray dataset.
2. Perform image preprocessing.
3. Resize images to **128 × 128** pixels.
4. Apply image augmentation.
5. Build a CNN using VGG19 Transfer Learning.
6. Train the model.
7. Validate model performance.
8. Save the trained model.
9. Deploy the model using Flask.
10. Predict pneumonia from uploaded X-ray images.

---

## 🧹 Image Preprocessing

The following preprocessing steps were applied:

- Image resizing (128 × 128)
- RGB image conversion
- Pixel normalization (1/255)
- Data augmentation

### Image Augmentation Techniques

- Random Rotation
- Horizontal Flip
- Width Shift
- Height Shift
- Shear Transformation

These augmentation techniques improve model robustness and reduce overfitting.

---

## 🧠 Model Architecture

The project uses **Transfer Learning** with the pretrained **VGG19** architecture.

### Base Model

- VGG19
- ImageNet pretrained weights
- Top layers removed (`include_top=False`)
- Base layers frozen during training

### Custom Classification Head

- Flatten Layer
- Dense Layer (4608 neurons, ReLU)
- Dropout (0.2)
- Dense Layer (1152 neurons, ReLU)
- Output Layer (2 neurons, Softmax)

This architecture enables the model to leverage pretrained image features while learning pneumonia-specific patterns.

---

## ⚙️ Training Configuration

### Optimizer

- SGD (Stochastic Gradient Descent)

### Learning Rate

- 0.0001

### Loss Function

- Categorical Crossentropy

### Callbacks Used

- EarlyStopping
- ModelCheckpoint
- ReduceLROnPlateau

These callbacks help improve training efficiency and reduce overfitting.

---

## 📈 Model Training

The model was trained using:

- ImageDataGenerator
- Batch image loading
- Data augmentation
- Validation dataset monitoring
- Early stopping for improved generalization

The trained model was saved in Keras format for deployment.

---

## 💻 Flask Web Application

A Flask-based web application was developed to make the model accessible through a graphical user interface.

### Features

- Upload Chest X-ray image
- Automatic preprocessing
- Real-time prediction
- Displays prediction as:
  - Normal
  - Pneumonia

This allows users to interact with the trained model without requiring programming knowledge.

---

## 📊 Prediction Workflow

```text
Chest X-ray Image
        │
        ▼
Image Upload
        │
        ▼
Preprocessing
        │
        ▼
Resize & Normalize
        │
        ▼
VGG19 CNN Model
        │
        ▼
Softmax Classification
        │
        ▼
Prediction
(Normal / Pneumonia)
```

---

## 💡 Key Features

- End-to-end deep learning pipeline
- Transfer Learning using VGG19
- Image augmentation
- Binary image classification
- Flask web deployment
- Real-time prediction
- Saved model for inference

---

## 📚 Key Learnings

- Gained hands-on experience with medical image classification.
- Learned Transfer Learning using pretrained CNN models.
- Understood image preprocessing techniques for deep learning.
- Applied data augmentation to improve model robustness.
- Learned to deploy deep learning models using Flask.
- Built a complete AI application from model training to deployment.

---

## 📁 Repository Structure

```text
Pneumonia Detection from Chest X-rays using CNN/
│
├── app.py
├── Pneumonia_Detection.ipynb
├── model.keras
├── model_weights/
├── chest_xray/
├── test_pneumonia_normal/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
├── uploads/
├── requirements.txt
└── README.md
```

---

## 🚀 Future Improvements

- Fine-tune VGG19 layers for improved performance.
- Compare multiple CNN architectures such as ResNet50, DenseNet121, and EfficientNet.
- Perform hyperparameter tuning.
- Generate Grad-CAM visualizations to explain model predictions.
- Deploy the application on a cloud platform for public access.
- Extend the model to classify multiple chest diseases instead of binary classification.

---

## 👩‍💻 Author

**Chaitra Pamidi**

Aspiring Data Scientist | Deep Learning | Computer Vision | Artificial Intelligence
