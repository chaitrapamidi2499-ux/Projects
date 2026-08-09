# 🧠 MBTI Personality Prediction using Natural Language Processing

> An NLP-based machine learning project that predicts Myers–Briggs Type Indicator (MBTI) personality types from textual data using text preprocessing, feature extraction, and machine learning classification.

---

# 📌 Overview

Personality prediction has applications in recruitment, recommendation systems, career guidance, and behavioral analytics. This project uses Natural Language Processing (NLP) and machine learning techniques to classify individuals into one of the 16 MBTI personality types based on their written text.

The project involves extensive text preprocessing, feature extraction using vectorization techniques, dimensionality reduction, and machine learning model evaluation using cross-validation.

---


# 📸 Project Preview

<img width="1202" height="671" alt="data_overview" src="https://github.com/user-attachments/assets/fa4e2531-468b-43ff-b796-10b6b2997e68" />
<img width="1172" height="632" alt="learning_curve_plot" src="https://github.com/user-attachments/assets/f6a89350-9fd9-4fdf-9428-c258b974ac37" />
<img width="1156" height="580" alt="personality_distribution" src="https://github.com/user-attachments/assets/e2b71843-d6ff-4dd7-a45b-c0c15ae95aae" />

---

# 🎯 Objectives

- Analyze MBTI personality text data.
- Clean and preprocess textual content.
- Convert text into numerical features.
- Build machine learning models for personality prediction.
- Compare model performance using cross-validation metrics.

---

# ✨ Features

- Text preprocessing and cleaning
- Stop-word removal
- Tokenization
- TF-IDF Vectorization
- Count Vectorization
- Dimensionality Reduction using Truncated SVD
- Machine Learning Classification
- Cross-validation
- Model performance comparison

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| NLP | NLTK, Regular Expressions |
| Feature Engineering | TF-IDF, Count Vectorizer |
| Machine Learning | Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Environment | Jupyter Notebook |

---

# 📂 Project Structure

```text
MBTI-Personality-Prediction/
│
├── mbti_personality_prediction.ipynb
├── mbti_dataset.csv
├── images/
└── README.md
```

---

# 📊 Dataset

The dataset contains user-generated text posts along with their corresponding Myers–Briggs personality types.

### Features

- Personality Type (Target)
- User Posts

### Target Classes

The model predicts one of the 16 MBTI personality types, including:

- INTJ
- INTP
- INFJ
- INFP
- ENTJ
- ENTP
- ENFJ
- ENFP
- ISTJ
- ISTP
- ISFJ
- ISFP
- ESTJ
- ESTP
- ESFJ
- ESFP

---

# 🔄 Project Workflow

```text
Dataset Loading
        │
        ▼
Text Cleaning
        │
        ▼
Tokenization
        │
        ▼
Stop-word Removal
        │
        ▼
Feature Extraction
(TF-IDF / Count Vectorizer)
        │
        ▼
Dimensionality Reduction
(Truncated SVD)
        │
        ▼
Model Training
        │
        ▼
Cross Validation
        │
        ▼
Personality Prediction
```

---

# 🤖 Machine Learning Models

The notebook evaluates two different NLP pipelines:

### Model 1

- TF-IDF Vectorizer
- Truncated SVD
- Extra Trees Classifier

### Model 2

- Count Vectorizer
- Multinomial Naive Bayes

---

# 📏 Model Performance

| Model | Cross Validation Accuracy | F1 Score |
|--------|--------------------------:|---------:|
| TF-IDF + Truncated SVD + Extra Trees | **29.51%** | **29.51%** |
| Count Vectorizer + Multinomial Naive Bayes | **56.37%** | **56.37%** |

### Best Performing Model

The **Count Vectorizer + Multinomial Naive Bayes** pipeline achieved the best performance with a **cross-validation accuracy of 56.37%**, outperforming the Extra Trees-based pipeline.

---

# 📈 Natural Language Processing Pipeline

The notebook includes:

- Text preprocessing
- URL and punctuation removal
- Stop-word removal
- Text normalization
- Count Vectorization
- TF-IDF Vectorization
- Truncated SVD
- Cross-validation
- Model comparison

---

# 🔍 Key Highlights

- Built an end-to-end NLP text classification pipeline.
- Compared two different feature extraction techniques.
- Reduced text dimensionality using Truncated SVD.
- Evaluated models using cross-validation.
- Predicted MBTI personality types from user-generated text.

---

# 🚀 Future Improvements

- Experiment with Word2Vec, GloVe, or FastText embeddings.
- Fine-tune transformer models such as BERT or RoBERTa.
- Address class imbalance using resampling techniques.
- Perform hyperparameter optimization.
- Deploy the prediction model as a web application using Streamlit or Flask.

---

# 📚 Learning Outcomes

Through this project, I gained hands-on experience in:

- Natural Language Processing (NLP)
- Text preprocessing techniques
- Feature extraction using TF-IDF and Count Vectorizer
- Dimensionality reduction using Truncated SVD
- Machine learning for text classification
- Cross-validation and model evaluation
- Personality prediction using textual data

---

# 👩‍💻 Author

**Chaitra Pamidi**  
*Data Analytics • Data Science • Machine Learning • Artificial Intelligence*

---

⭐ **If you found this project interesting, feel free to explore the repository and connect with me!**
