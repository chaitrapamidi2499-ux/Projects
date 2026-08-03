# 🚗 Automobile Price Analysis using Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project focuses on performing **Exploratory Data Analysis (EDA)** on an automobile dataset to understand vehicle characteristics, pricing trends, fuel efficiency, and manufacturer distribution. The analysis also includes data preprocessing techniques such as outlier detection and missing value treatment to prepare the dataset for further predictive modeling.

---

## 🎯 Problem Statement

Automobile datasets often contain numerous numerical and categorical features that influence vehicle pricing and performance. Before developing predictive models, it is essential to understand the dataset, identify inconsistencies, detect outliers, and handle missing values.

The objective of this project is to perform a comprehensive exploratory data analysis to uncover patterns, improve data quality, and prepare the dataset for future machine learning applications.

---

## 📂 Dataset

**Dataset:** Car Features and MSRP

The dataset contains information about various automobile models, including:

- Manufacturer
- Model
- Year
- Engine Fuel Type
- Engine HP
- Engine Cylinders
- Transmission Type
- Driven Wheels
- Number of Doors
- Market Category
- Vehicle Size
- Vehicle Style
- Highway MPG
- City MPG
- Popularity
- MSRP

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## ⚙️ Project Workflow

- Imported the automobile dataset
- Identified numerical and categorical variables
- Performed descriptive statistical analysis
- Explored feature distributions
- Compared fuel efficiency across manufacturers
- Analyzed categorical variables
- Detected outliers using the Interquartile Range (IQR) method
- Identified missing values
- Applied missing value treatment
- Validated the cleaned dataset

---

## 📊 Exploratory Data Analysis

The analysis includes:

- Summary statistics
- Mean and median analysis
- Frequency distribution
- Manufacturer-wise analysis
- Vehicle size distribution
- Transmission type analysis
- Fuel efficiency comparison
- Outlier detection
- Missing value analysis

---

## 💡 Key Findings

- The dataset contains both numerical and categorical automobile attributes.
- The average MSRP is approximately **$40,595**, indicating that the dataset primarily consists of mid-to-high-priced vehicles.
- Highway fuel efficiency was compared across **BMW, Audi, and Mercedes-Benz**, with BMW showing the highest average highway MPG among the selected manufacturers.
- The dataset contains **48 automobile manufacturers**.
- **Chevrolet** appears most frequently in the dataset, while **Bugatti, Spyker, and Genesis** are among the least represented manufacturers.
- Automatic transmission vehicles are more common than manual vehicles.
- Compact vehicles represent the largest vehicle size category in the dataset.
- Outliers were identified using the **Interquartile Range (IQR)** method.
- Missing values were detected and successfully treated for multiple attributes, resulting in a clean dataset with **no remaining missing values**.

---

## 🧹 Data Cleaning

Missing values were handled for the following variables:

- Engine Fuel Type
- Engine HP
- Market Category
- Engine Cylinders
- Number of Doors

The dataset was validated after preprocessing to ensure that no missing values remained.

---

## 📁 Repository Structure

```
Automobile Price Analysis using Exploratory Data Analysis/
│
├── Car Features and MSRP(EDA).ipynb
├── Car features and MSRP.csv
└── README.md
```

---

## 🚀 Future Improvements

- Perform feature engineering
- Build regression models for MSRP prediction
- Develop an interactive dashboard for business users
- Perform advanced correlation and feature importance analysis

---

## 👩‍💻 Author

**Chaitra Pamidi**

Data Science | Machine Learning | Artificial Intelligence
