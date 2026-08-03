# 🚘 Automobile Sales Price Prediction using Regression

## 📌 Project Overview

This project focuses on developing regression models to predict automobile sales values using dealership data. The workflow includes data preprocessing, outlier handling, feature encoding, model training, and performance evaluation using multiple machine learning regression algorithms.

---

## 🎯 Problem Statement

Accurate sales prediction helps automobile dealerships make informed decisions regarding inventory planning, pricing strategies, and business forecasting.

The objective of this project is to build regression models capable of predicting automobile sales while comparing different machine learning algorithms to identify the best-performing model.

---

## 📂 Dataset

**Dataset:** Dealership Data

The dataset contains dealership and automobile-related information used to predict vehicle sales.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## ⚙️ Project Workflow

- Imported and explored the dataset
- Performed descriptive data analysis
- Checked for missing values
- Removed outliers using the Interquartile Range (IQR) method
- Applied One-Hot Encoding to categorical variables
- Split the dataset into training and testing sets (75:25)
- Trained multiple regression models
- Evaluated model performance using Mean Absolute Percentage Error (MAPE)

---

## 🤖 Machine Learning Models

The following regression models were implemented and compared:

- Linear Regression
- K-Nearest Neighbors (KNN) Regressor
- Decision Tree Regressor

---

## 📊 Model Evaluation

Model performance was evaluated using **Mean Absolute Percentage Error (MAPE)**.

| Model | Train MAPE | Test MAPE |
|--------|-----------:|----------:|
| Linear Regression | 0.0815 | **0.1054** |
| Decision Tree Regressor | 0.1154 | 0.1112 |
| KNN Regressor | Evaluated for K = 1–19 | Performance comparison performed |

---

## 💡 Key Findings

- The dataset was successfully preprocessed by handling outliers and encoding categorical variables.
- One-Hot Encoding was applied to transform categorical features into numerical representations.
- Multiple regression algorithms were compared to evaluate predictive performance.
- Based on the evaluation metric (MAPE), **Linear Regression achieved the lowest test error** among the implemented models.

---

## 📁 Repository Structure

```
Automobile Sales Price Prediction using Regression/
│
├── Dealership_Data(Regression).ipynb
├── Dealership_Data.csv
└── README.md
```

---

## 🚀 Future Improvements

- Perform feature selection and feature engineering.
- Experiment with ensemble regression models such as Random Forest and XGBoost.
- Tune hyperparameters using GridSearchCV.
- Evaluate models using additional metrics such as RMSE and R² Score.

---

## 👩‍💻 Author

**Chaitra Pamidi**

Data Science | Machine Learning | Artificial Intelligence
