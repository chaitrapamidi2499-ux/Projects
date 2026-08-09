# 🚗 Automobile Price Prediction

> A machine learning project that predicts automobile prices based on vehicle specifications using regression algorithms.

---

# 📌 Overview

Accurate automobile price prediction helps manufacturers, dealerships, and buyers make informed decisions. This project builds and evaluates multiple machine learning regression models to estimate vehicle prices using various automobile specifications.

The project includes data preprocessing, outlier treatment, feature engineering, model training, and performance evaluation to identify the most suitable regression model.

---

# 📸 Project Preview

<img width="1075" height="887" alt="dataset_overview" src="https://github.com/user-attachments/assets/bb8c5ca5-8bcc-4caa-987b-8254b65fb28e" />
<img width="1092" height="915" alt="outliers_detection" src="https://github.com/user-attachments/assets/610ad158-1a82-445f-ab07-010a6cfb8ff9" />
<img width="1012" height="810" alt="train_test_split" src="https://github.com/user-attachments/assets/8974c529-bcc9-4c13-a4f7-3123387bea3c" />
<img width="1165" height="332" alt="decision_tree" src="https://github.com/user-attachments/assets/65cfe86c-e935-490f-88c3-8f4b6b66a16c" />
<img width="1195" height="347" alt="linear_regression" src="https://github.com/user-attachments/assets/c3da7cc1-b079-4f70-af04-827ffeb02c20" />
<img width="1107" height="747" alt="MAPE_Scores_KNN" src="https://github.com/user-attachments/assets/509d8391-77de-42d8-9d17-af2c207e4919" />

---

# 🎯 Objectives

- Clean and preprocess automobile data.
- Handle missing values and outliers.
- Prepare features for machine learning.
- Train multiple regression models.
- Compare model performance using evaluation metrics.
- Predict automobile prices accurately.

---

# ✨ Features

- Data preprocessing
- Outlier detection using IQR
- Feature encoding
- Train-test split
- Multiple regression models
- Model performance comparison
- Price prediction

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Libraries | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Environment | Jupyter Notebook |

---

# 📂 Project Structure

```text
Automobile-Price-Prediction/
│
├── automobile_price_prediction.ipynb
├── automobile_dataset.csv
├── images/
└── README.md
```

---

# 📊 Dataset

The dataset contains automobile specifications and their corresponding market prices.

### Key Features

- Make
- Model
- Year
- Engine HP
- Engine Cylinders
- Number of Doors
- Highway MPG
- City MPG
- Vehicle Size
- Vehicle Style
- Transmission Type
- Driven Wheels
- Market Category

**Target Variable**

- MSRP (Automobile Price)

---

# 🔄 Project Workflow

```text
Dataset Loading
        │
        ▼
Data Cleaning
        │
        ▼
Missing Value Handling
        │
        ▼
Outlier Removal (IQR)
        │
        ▼
Feature Engineering
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
Price Prediction
```

---

# 🤖 Machine Learning Models

The following regression algorithms were implemented and evaluated:

- Linear Regression
- K-Nearest Neighbors (KNN) Regressor
- Decision Tree Regressor

---

# 📏 Model Evaluation

The models were evaluated using:

- Mean Absolute Percentage Error (MAPE)
- Training Performance
- Testing Performance

The comparison helps identify the model that generalizes best on unseen data.

# 📏 Model Performance

| Model | Train MAPE | Test MAPE |
|--------|-----------:|----------:|
| Linear Regression | **8.15%** | **10.54%** |
| K-Nearest Neighbors (K=5) | **22.68%** | **26.13%** |
| Decision Tree Regressor | **11.54%** | **11.12%** |

### Best Performing Model

Based on the evaluation results, **Linear Regression** achieved the lowest prediction error with a **Test MAPE of 10.54%**, making it the best-performing model for this dataset. The Decision Tree Regressor also demonstrated competitive performance with a Test MAPE of **11.12%**, while the K-Nearest Neighbors Regressor produced comparatively higher prediction errors.
---

# 🔍 Key Highlights

- Performed complete data preprocessing before training.
- Removed outliers using the Interquartile Range (IQR) method.
- Compared multiple regression algorithms.
- Evaluated model performance using MAPE.
- Built a reusable workflow for automobile price prediction.

---

# 🚀 Future Improvements

- Implement ensemble models such as Random Forest and XGBoost.
- Perform hyperparameter tuning using GridSearchCV.
- Deploy the model using Streamlit or Flask.
- Improve feature engineering for higher prediction accuracy.
- Build an interactive web application for real-time predictions.

---

# 📚 Learning Outcomes

Through this project, I gained hands-on experience in:

- Data preprocessing
- Outlier detection and removal
- Feature engineering
- Regression algorithms
- Model evaluation using MAPE
- Comparing multiple machine learning models
- Building end-to-end regression workflows

---

# 👩‍💻 Author

**Chaitra Pamidi**  
*Data Analytics • Data Science • Machine Learning • Artificial Intelligence*

---

⭐ **If you found this project interesting, feel free to explore the repository and connect with me!**
