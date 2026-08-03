# ❤️ Heart Disease Prediction using Machine Learning

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide, making early diagnosis crucial for effective treatment and prevention. This project develops and evaluates multiple machine learning classification models to predict the presence of heart disease using patient clinical data.

The project follows a complete machine learning workflow, including data preprocessing, exploratory data analysis (EDA), outlier detection, feature engineering, model development, and performance evaluation. Three classification algorithms were implemented and compared to determine the most effective model for heart disease prediction.

---

## 🎯 Problem Statement

Accurately predicting heart disease based on a patient's medical information can assist healthcare professionals in identifying high-risk individuals and supporting early clinical decision-making.

The objective of this project is to build predictive machine learning models capable of classifying whether a patient is likely to have heart disease using various health-related attributes.

---

## 🎯 Objectives

- Understand the characteristics of the heart disease dataset.
- Perform exploratory data analysis to identify important patterns.
- Detect and handle outliers.
- Prepare the dataset for machine learning.
- Train multiple classification algorithms.
- Compare model performance using evaluation metrics.
- Identify the best-performing classification model.

---

## 📂 Dataset

**Dataset:** Heart Disease Dataset

The dataset contains patient health information collected from clinical examinations.

### Features include:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG Results
- Maximum Heart Rate
- Exercise-Induced Angina
- ST Depression (Oldpeak)
- Slope of Peak Exercise ST Segment
- Number of Major Vessels
- Thalassemia
- Target Variable (Presence of Heart Disease)

---

## 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## ⚙️ Project Workflow

1. Import the dataset.
2. Explore the dataset structure.
3. Check data types and summary statistics.
4. Detect missing values.
5. Perform Exploratory Data Analysis (EDA).
6. Identify and remove outliers using the IQR method.
7. Encode categorical variables where required.
8. Split the dataset into training and testing datasets.
9. Train multiple machine learning classification models.
10. Evaluate and compare model performance.

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed before model training:

- Dataset inspection
- Statistical summary generation
- Missing value verification
- Outlier detection using the Interquartile Range (IQR) method
- Removal of extreme outliers
- Feature and target variable separation
- Train-test split for model evaluation

---

## 📊 Exploratory Data Analysis

The notebook includes several visualizations to better understand the dataset, including:

- Class distribution
- Feature distributions
- Box plots for outlier detection
- Correlation heatmap
- Relationship between important medical attributes
- Statistical summaries

EDA helped identify feature distributions and detect potential anomalies before model development.

---

## 🤖 Machine Learning Models

The following supervised learning algorithms were implemented and compared:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree Classifier

---

## 📈 Model Performance

The models were evaluated using classification accuracy on both the training and testing datasets.

| Model | Training Accuracy | Testing Accuracy |
|--------|------------------:|-----------------:|
| Logistic Regression | **87.56%** | **81.46%** |
| K-Nearest Neighbors (KNN) | **97.80%** | **92.68%** |
| Decision Tree | **100.00%** | **98.54%** |

### Best Performing Model

The **Decision Tree Classifier** achieved the highest testing accuracy of **98.54%**.

However, since it achieved **100% training accuracy**, the model may be slightly overfitting the training data. This highlights the importance of balancing model complexity and generalization.

---

## 📊 Evaluation Metrics

The models were evaluated using:

- Training Accuracy
- Testing Accuracy

The notebook compares the performance of all implemented algorithms to identify the most suitable model for heart disease prediction.

---

## 💡 Key Findings

- Successfully completed an end-to-end machine learning classification workflow.
- Performed data preprocessing before model development.
- Detected and handled outliers using the IQR method.
- Compared three supervised classification algorithms.
- Decision Tree achieved the highest testing accuracy (**98.54%**).
- K-Nearest Neighbors also performed well with a testing accuracy of **92.68%**.
- Logistic Regression provided a reliable baseline model with **81.46%** testing accuracy.
- The perfect training accuracy of the Decision Tree suggests possible overfitting.

---

## 📚 Key Learnings

- Learned the complete workflow of a supervised machine learning classification project.
- Gained practical experience in exploratory data analysis and feature understanding.
- Understood the importance of preprocessing before model training.
- Learned how different classification algorithms perform on the same dataset.
- Explored the impact of model complexity on generalization.
- Developed skills in evaluating classification models using training and testing accuracy.

---

## 📁 Repository Structure

```text
Heart Disease Prediction using Machine Learning/
│
├── Heart_Disease_Prediction.ipynb
├── heartdisease.csv
└── README.md
```

---

## 🚀 Future Improvements

- Perform feature selection to identify the most influential clinical variables.
- Apply hyperparameter tuning using GridSearchCV or RandomizedSearchCV.
- Evaluate ensemble methods such as Random Forest and XGBoost.
- Perform cross-validation for more reliable model evaluation.
- Deploy the trained model as an interactive web application using Flask or Streamlit.
- Incorporate Explainable AI (XAI) techniques such as SHAP or LIME to improve model interpretability.

---

## 👩‍💻 Author

**Chaitra Pamidi**

Aspiring Data Scientist | Machine Learning | Artificial Intelligence | Data Analytics
