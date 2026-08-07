# ❤️ Heart Disease Prediction using Machine Learning

> A machine learning project that predicts the likelihood of heart disease using patient health attributes and compares multiple classification algorithms to identify the best-performing model.

---

# 📌 Overview

Heart disease is one of the leading causes of mortality worldwide. Early prediction can assist healthcare professionals in making timely diagnoses and treatment decisions.

This project develops a machine learning-based prediction system that classifies whether a patient is likely to have heart disease based on clinical and demographic attributes. Multiple classification algorithms are implemented and compared to determine the most effective model.

---

# 🎯 Objectives

- Analyze the heart disease dataset.
- Perform data preprocessing and feature scaling.
- Train multiple machine learning classification models.
- Compare model performance using evaluation metrics.
- Predict the likelihood of heart disease accurately.

---

# ✨ Features

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature scaling using StandardScaler
- Logistic Regression classifier
- K-Nearest Neighbors (KNN) classifier
- Decision Tree classifier
- Model evaluation and comparison
- Confusion Matrix visualization
- Threshold-based prediction analysis

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Libraries | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Statistical Analysis | Statsmodels |
| Environment | Jupyter Notebook |

---

# 📂 Project Structure

```text
Heart-Disease-Prediction/
│
├── heart_disease_prediction.ipynb
├── heart_disease_data.csv
├── images/
└── README.md
```

---

# 📊 Dataset

The dataset consists of **1,025 patient records** with **14 clinical attributes** used to predict the presence of heart disease.

### Features

- Age
- Sex
- Chest Pain Type (cp)
- Resting Blood Pressure (trestbps)
- Cholesterol (chol)
- Fasting Blood Sugar (fbs)
- Resting ECG (restecg)
- Maximum Heart Rate (thalach)
- Exercise-Induced Angina (exang)
- ST Depression (oldpeak)
- Slope
- Number of Major Vessels (ca)
- Thalassemia (thal)

**Target Variable**

- Heart Disease (0 = No Disease, 1 = Disease)

---

# 🔄 Project Workflow

```text
Dataset Loading
        │
        ▼
Data Exploration
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Scaling
        │
        ▼
Train-Test Split
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Heart Disease Prediction
```

---

# 🤖 Machine Learning Models

The following classification algorithms were implemented:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree Classifier

---

# 📏 Model Performance

| Model | Train Accuracy | Test Accuracy |
|--------|---------------:|--------------:|
| Logistic Regression | **81.46%** | **87.56%** |
| K-Nearest Neighbors (K=3) | **97.80%** | **92.68%** |
| Decision Tree Classifier | **100.00%** | **98.54%** |

### Best Performing Model

The **Decision Tree Classifier** achieved the highest performance with a **Test Accuracy of 98.54%**. The notebook also evaluates probability thresholds and visualizes performance using a confusion matrix.

---

# 📈 Exploratory Data Analysis

The project includes:

- Dataset inspection
- Missing value analysis
- Statistical summary
- Distribution analysis
- Correlation analysis
- Feature scaling
- Confusion Matrix visualization

---

# 🔍 Key Highlights

- Compared three supervised machine learning algorithms.
- Applied feature scaling before model training.
- Evaluated models using training and testing accuracy.
- Performed threshold-based probability analysis.
- Visualized prediction performance using a confusion matrix.
- Identified the Decision Tree Classifier as the best-performing model on the dataset.

---

# 📸 Outputs

<img width="1206" height="782" alt="dataset_overview" src="https://github.com/user-attachments/assets/1e8faffe-079c-45d3-952d-f5b5ce79469d" />
<img width="1202" height="902" alt="model_comparison" src="https://github.com/user-attachments/assets/d5622f75-8841-440a-8745-06fd62207120" />
<img width="1206" height="912" alt="correlation_heatmap" src="https://github.com/user-attachments/assets/6df32be0-a558-46ad-b85a-5006219c649b" />
<img width="1182" height="885" alt="DT_ROC_curve" src="https://github.com/user-attachments/assets/eba7f044-e4bc-4168-90ec-10f3a960be7f" />
<img width="1202" height="910" alt="KNN_ROC_curve" src="https://github.com/user-attachments/assets/0ce05bc0-09fa-4ba9-a1c6-c65337d31d9a" />
<img width="1190" height="832" alt="LR_ROC_curve" src="https://github.com/user-attachments/assets/678319a7-3e49-4840-b3d0-81a88da068a7" />


---

# 🚀 Future Improvements

- Implement ensemble methods such as Random Forest and XGBoost.
- Perform hyperparameter tuning using GridSearchCV.
- Develop a web application using Streamlit or Flask.
- Integrate feature importance analysis.
- Validate the model on external healthcare datasets.

---

# 📚 Learning Outcomes

Through this project, I gained hands-on experience in:

- Data preprocessing
- Feature scaling
- Classification algorithms
- Model comparison
- Confusion Matrix interpretation
- Threshold optimization
- Machine learning model evaluation
- Healthcare predictive analytics

---

# 👩‍💻 Author

**Chaitra Pamidi**  
*Data Analytics • Data Science • Machine Learning • Artificial Intelligence*

---

⭐ **If you found this project interesting, feel free to explore the repository and connect with me!**
