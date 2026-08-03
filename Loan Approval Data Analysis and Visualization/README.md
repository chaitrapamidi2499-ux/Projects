# 💳 Loan Status Analysis using Exploratory Data Analysis (EDA)

## 📌 Project Overview

Loan approval decisions depend on several applicant attributes such as income, employment history, credit behavior, and financial obligations. This project performs Exploratory Data Analysis (EDA) on a loan dataset to understand the characteristics of loan applicants and identify factors that may influence loan approval.

The analysis focuses on data exploration, preprocessing, outlier detection, statistical summaries, and visualization to uncover meaningful insights from the dataset.

---

## 🎯 Problem Statement

Financial institutions process thousands of loan applications, making it essential to understand applicant characteristics before making lending decisions.

The objective of this project is to analyze loan application data, identify important trends, detect anomalies, and gain insights into factors associated with loan approval status.

---

## 🎯 Objectives

- Explore the structure of the loan dataset.
- Perform statistical analysis of applicant information.
- Analyze categorical and numerical variables.
- Detect and visualize outliers.
- Study relationships between important financial variables.
- Identify patterns associated with loan approval.

---

## 📂 Dataset

**Dataset:** Loan Status Dataset

The dataset contains applicant demographic and financial information along with loan approval status.

Some of the attributes analyzed include:

- Loan Status
- Current Loan Amount
- Annual Income
- Years in Current Job
- Purpose of Loan
- Monthly Debt
- Credit Score
- Home Ownership
- Tax Liens
- Number of Credit Problems
- Bankruptcy Records
- Other applicant financial information

---

## 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## ⚙️ Project Workflow

1. Import the dataset.
2. Inspect dataset structure.
3. Generate descriptive statistics.
4. Analyze categorical variables.
5. Check class distributions.
6. Detect outliers using the IQR method.
7. Visualize numerical features.
8. Analyze feature relationships using correlation and covariance.
9. Explore important business questions through visualizations.

---

## 🧹 Data Exploration & Preprocessing

The notebook includes:

- Dataset inspection
- Data type verification
- Descriptive statistics
- Summary statistics for categorical variables
- Loan Status frequency analysis
- Years in Current Job analysis
- Outlier detection using the Interquartile Range (IQR) method
- Box plot visualization for numerical variables

---

## 📊 Exploratory Data Analysis

The notebook performs several exploratory analyses, including:

### Loan Status Distribution
- Examines the frequency of approved and rejected loans.

### Employment Analysis
- Analyzes the distribution of applicants based on **Years in Current Job**.

### Outlier Detection
- Uses the **IQR (Interquartile Range)** method to identify outliers across numerical features.
- Box plots are generated for numerical variables.

### Correlation Analysis
- Correlation heatmap to understand relationships among numerical features.

### Covariance Analysis
- Covariance heatmap for studying feature relationships.

### Loan Amount Distribution
- Histogram with KDE showing the distribution of **Current Loan Amount**.

### Loan Purpose Analysis
- Identifies the most common purposes for loan applications.

### Annual Income Analysis
- Compares Annual Income across different Loan Status categories using box plots.

---

## 📈 Key Insights

The notebook explores several business questions, including:

- Distribution of loan approval status.
- Employment history of applicants.
- Distribution of current loan amounts.
- Most common loan purposes.
- Relationship between applicant annual income and loan approval.
- Correlation among numerical financial variables.
- Presence of outliers in financial attributes.

---

## 💡 Key Findings

- Conducted comprehensive exploratory data analysis on a real-world loan dataset.
- Identified class distribution for loan approval status.
- Examined applicant employment history.
- Detected potential outliers using the IQR method.
- Visualized numerical feature distributions.
- Explored relationships between financial variables using correlation and covariance heatmaps.
- Compared applicant annual income across different loan approval categories.

---

## 📚 Key Learnings

- Learned how to perform structured exploratory data analysis.
- Gained experience interpreting statistical summaries.
- Understood the importance of identifying outliers before model development.
- Improved skills in visualizing financial datasets.
- Learned how correlation and covariance help understand feature relationships.
- Practiced converting business questions into data-driven analyses.

---

## 📁 Repository Structure

```text
Loan Status Analysis/
│
├── Loan_Status_Analysis.ipynb
├── Loan Status.csv
└── README.md
```

---

## 🚀 Future Improvements

- Handle missing values using advanced imputation techniques.
- Perform feature engineering for better financial insights.
- Build machine learning models to predict loan approval.
- Compare multiple classification algorithms.
- Develop an interactive dashboard for loan analytics.
- Deploy the project as a web application for real-time loan assessment.

---

## 👩‍💻 Author

**Chaitra Pamidi**

Aspiring Data Scientist | Machine Learning | Artificial Intelligence | Data Analytics
