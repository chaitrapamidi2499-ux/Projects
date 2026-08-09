# 💰 Loan Data Analysis

> A data analysis project that explores loan applicant data through data cleaning, preprocessing, exploratory data analysis (EDA), and business insights to understand loan characteristics and borrower behavior.

---

# 📌 Overview

This project performs an in-depth analysis of a loan dataset to understand borrower characteristics, loan status, and financial patterns. The analysis includes data cleaning, handling missing values, outlier treatment, statistical analysis, and visualization to uncover meaningful insights that can support financial decision-making.

The project demonstrates a complete data preprocessing and exploratory data analysis workflow using Python.

---

# 📸 Project Preview

<img width="1250" height="846" alt="dataset_overview" src="https://github.com/user-attachments/assets/d160905d-565a-4ca0-a21d-4a30ee66f445" />
<img width="1207" height="841" alt="loan_status" src="https://github.com/user-attachments/assets/8e9704aa-8497-457b-b66b-1e42580d40c7" />
<img width="1247" height="907" alt="distribution_annual_income" src="https://github.com/user-attachments/assets/8ac5daae-6043-448a-9730-911d0c4b1be6" />
<img width="1062" height="911" alt="covariance" src="https://github.com/user-attachments/assets/b39f742e-ec1f-4697-a01a-66e92879c260" />
<img width="1030" height="907" alt="correlation_heatmap" src="https://github.com/user-attachments/assets/91326d87-dec6-49e6-853a-175c00270537" />

---

# 🎯 Objectives

- Explore the loan dataset and understand its structure.
- Clean and preprocess the data.
- Handle missing values using appropriate statistical techniques.
- Detect and treat outliers.
- Analyze borrower demographics and loan characteristics.
- Generate business insights through data visualization.

---

# ✨ Features

- Data exploration
- Data preprocessing
- Missing value treatment
- Duplicate record detection
- Outlier detection using IQR
- Outlier capping
- Correlation analysis
- Covariance analysis
- Distribution analysis
- Business insight generation

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Libraries | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Missingno |
| Environment | Jupyter Notebook |

---

# 📂 Project Structure

```text
Loan-Data-Analysis/
│
├── loan_analysis.ipynb
├── loan_status_data.csv
├── images/
└── README.md
```

---

# 📊 Dataset

The dataset contains loan application records with customer financial and credit information.

### Key Features

- Loan ID
- Customer ID
- Loan Status
- Current Loan Amount
- Term
- Credit Score
- Annual Income
- Years in Current Job
- Home Ownership
- Purpose
- Monthly Debt
- Years of Credit History
- Number of Open Accounts
- Number of Credit Problems
- Current Credit Balance
- Maximum Open Credit
- Bankruptcies
- Tax Liens

---

# 🔄 Project Workflow

```text
Dataset Loading
        │
        ▼
Data Inspection
        │
        ▼
Data Cleaning
        │
        ▼
Missing Value Treatment
        │
        ▼
Outlier Detection & Capping
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Correlation & Covariance Analysis
        │
        ▼
Business Insights
```

---

# 📈 Exploratory Data Analysis

The notebook includes:

- Dataset overview
- Data type inspection
- Summary statistics
- Missing value analysis
- Missing value visualization using Missingno
- Duplicate record detection
- Outlier detection using the IQR method
- Outlier treatment through capping
- Correlation heatmap
- Covariance heatmap
- Distribution plots
- Box plots
- Count plots
- Crosstab analysis
- Grouped statistical analysis

---

# 🔍 Business Questions Answered

The analysis addresses several business questions, including:

- What is the distribution of current loan amounts?
- How does loan status vary across different loan terms?
- What are the most common loan purposes?
- How does annual income differ by loan status?
- How does home ownership influence years of credit history?
- What is the average loan amount for each loan purpose?

---

# 📊 Data Preprocessing Highlights

- Renamed columns for consistency.
- Removed duplicate records.
- Treated missing values using median, mode, and domain-specific values.
- Filtered unrealistic credit scores above 850.
- Detected outliers using the Interquartile Range (IQR) method.
- Applied outlier capping to numerical features.
- Encoded the target variable for future machine learning applications.

---

# 🚀 Future Improvements

- Develop a machine learning model for loan approval prediction.
- Perform feature engineering.
- Apply feature selection techniques.
- Compare multiple classification algorithms.
- Deploy the prediction model using Streamlit or Flask.

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Data preprocessing
- Missing value treatment
- Outlier detection and handling
- Exploratory Data Analysis (EDA)
- Correlation and covariance analysis
- Business data visualization
- Statistical analysis using Python

---

# 👩‍💻 Author

**Chaitra Pamidi**  
*Data Analytics • Data Science • Machine Learning • Artificial Intelligence*

---

⭐ **If you found this project interesting, feel free to explore the repository and connect with me!**
