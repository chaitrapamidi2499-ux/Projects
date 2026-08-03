# 🧠 Personality Prediction using NLP and Machine Learning

## 📌 Project Overview

Understanding personality traits from written text has applications in personalized recommendations, behavioral analysis, recruitment, and social media analytics. This project predicts Myers–Briggs Type Indicator (MBTI) personality types by applying Natural Language Processing (NLP) techniques to users' social media posts.

The project follows a complete NLP pipeline, including text preprocessing, feature extraction using TF-IDF, dimensionality reduction, machine learning model development, and performance evaluation using cross-validation.

---

## 🎯 Problem Statement

People express their personalities through the language they use online. By analyzing textual data, machine learning models can identify linguistic patterns associated with different MBTI personality types.

The objective of this project is to classify users into one of the sixteen MBTI personality categories based on their written posts.

---

## 🎯 Objectives

- Explore the MBTI personality dataset.
- Clean and preprocess textual data.
- Convert text into numerical representations using TF-IDF.
- Reduce feature dimensionality.
- Train multiple machine learning models.
- Evaluate model performance using cross-validation.
- Compare different classification approaches.

---

## 📂 Dataset

**Dataset:** MBTI Personality Prediction Dataset

The dataset consists of social media posts along with the corresponding MBTI personality type.

### Main Features

- Personality Type (Target Variable)
- User Posts

The target variable contains the 16 Myers–Briggs personality categories, including:

- INFJ
- INFP
- INTJ
- INTP
- ENFJ
- ENFP
- ENTJ
- ENTP
- ISFJ
- ISFP
- ISTJ
- ISTP
- ESFJ
- ESFP
- ESTJ
- ESTP

---

## 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Matplotlib
- Seaborn

---

## ⚙️ Project Workflow

1. Load the MBTI dataset.
2. Explore the dataset structure.
3. Clean and preprocess text data.
4. Remove unnecessary characters and noise.
5. Prepare cleaned text for NLP.
6. Convert text into TF-IDF vectors.
7. Apply dimensionality reduction using Truncated SVD.
8. Train machine learning models.
9. Evaluate models using cross-validation.
10. Generate personality predictions for unseen text.

---

## 🧹 Text Preprocessing

The notebook performs several NLP preprocessing steps, including:

- Text cleaning
- Lowercase conversion
- Removal of unwanted characters
- Stop-word removal
- Token processing
- Preparation of cleaned posts for vectorization

These steps help improve the quality of text features before model training.

---

## 🔤 Feature Engineering

The project uses the following NLP techniques:

- **TF-IDF Vectorization** for converting text into numerical feature vectors.
- **Truncated Singular Value Decomposition (SVD)** for dimensionality reduction and efficient model training.

---

## 🤖 Machine Learning Models

Two machine learning pipelines were implemented and compared:

### Extra Trees Classifier Pipeline

- TF-IDF Vectorizer
- Truncated SVD
- Extra Trees Classifier

### Logistic Regression Pipeline

- TF-IDF Vectorizer
- Logistic Regression

---

## 📈 Model Performance

Performance was evaluated using 5-fold cross-validation.

| Model | Cross-Validation Accuracy | F1 Score |
|--------|--------------------------:|---------:|
| Extra Trees Classifier | **28.76%** | **28.76%** |
| Logistic Regression | **56.37%** | **56.37%** |

### Best Performing Model

The **Logistic Regression** model outperformed the Extra Trees Classifier, achieving a cross-validation accuracy of **56.37%**.

---

## 📊 Evaluation Metrics

The notebook evaluates the models using:

- Cross-Validation Accuracy
- F1 Score (Micro)
- Log Loss

This enables a fair comparison of different classification approaches on the same dataset.

---

## 💡 Key Findings

- Successfully built an end-to-end NLP classification pipeline.
- Cleaned and preprocessed textual data before model development.
- Converted text into numerical representations using TF-IDF.
- Applied dimensionality reduction using Truncated SVD.
- Compared two machine learning pipelines.
- Logistic Regression achieved the best cross-validation accuracy (**56.37%**).
- Generated personality predictions for new user comments.

---

## 📚 Key Learnings

- Learned how to preprocess textual datasets for NLP tasks.
- Gained practical experience with TF-IDF feature extraction.
- Understood the importance of dimensionality reduction for high-dimensional text data.
- Compared different machine learning algorithms for multiclass text classification.
- Learned to evaluate NLP models using cross-validation and F1 score.

---

## 📁 Repository Structure

```text
Personality Prediction using NLP/
│
├── Personality_Prediction_NLP.ipynb
├── mbti_1.csv
├── ForumMessages.csv
├── Users.csv
└── README.md
```

---

## 🚀 Future Improvements

- Experiment with Word2Vec, FastText, or GloVe embeddings.
- Fine-tune transformer-based models such as BERT or RoBERTa.
- Perform hyperparameter tuning to improve classification performance.
- Address class imbalance using resampling techniques.
- Develop a web application where users can enter text and receive personality predictions.
- Compare traditional machine learning models with deep learning approaches.

---

## 👩‍💻 Author

**Chaitra Pamidi**

Aspiring Data Scientist | Machine Learning | Natural Language Processing | Artificial Intelligence
