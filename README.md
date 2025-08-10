# Question Pairs Semantic Meaning Detector

A simple **Streamlit web app** that detects whether two questions are semantically similar (duplicates) using a pre-trained machine learning model.

## 🚀 Live Demo
🔗 [think-alike](https://think-alike.streamlit.app/) – Try it out in your browser!
---
Dataset Link- https://www.kaggle.com/c/quora-question-pairs

## 🛠 Tech Stack
- **Python 3.9+**
- **Streamlit** – Frontend framework
- **Scikit-learn** – ML model loading and prediction
- **NLTK** – Text preprocessing (stopwords)
- **Pickle** – Model storage
- **Custom CSS** – UI styling
- **Bag of Words (BoW)** – Text vectorization for model input
- **HMM (Hidden Markov Model)** – Sequence modeling for question similarity
- **Random Forest Classifier** – Baseline classification model
- **XGBoost** – Gradient boosting for improved accuracy
- **Advanced Feature Engineering** – Token features, length-based features, fuzzy matching

---

## ⚙️ How It Works

### 1️⃣ Text Preprocessing
- Lowercasing, removing punctuation and special characters  
- Decontracting words (e.g., "can't" → "cannot")  
- Removing stopwords using NLTK  
- Stemming/Lemmatization for word normalization  

### 2️⃣ Feature Engineering
#### **Bag of Words (BoW)**
- Converts cleaned questions into numerical vectors based on word frequency.  

#### **Advanced Features**
1. **Token Features**
   - `cwc_min` – Ratio of common words to smaller question length  
   - `cwc_max` – Ratio of common words to larger question length  
   - `csc_min` – Ratio of common stopwords to smaller stopword count  
   - `csc_max` – Ratio of common stopwords to larger stopword count  
   - `ctc_min` – Ratio of common tokens to smaller token count  
   - `ctc_max` – Ratio of common tokens to larger token count  
   - `last_word_eq` – 1 if last words match, else 0  
   - `first_word_eq` – 1 if first words match, else 0  

2. **Length-Based Features**
   - `mean_len` – Mean number of words in both questions  
   - `abs_len_diff` – Absolute word count difference  
   - `longest_substr_ratio` – Longest common substring length ratio  

3. **Fuzzy Matching Features** (using `fuzzywuzzy`)
   - `fuzz_ratio` – Basic similarity score  
   - `fuzz_partial_ratio` – Partial match score  
   - `token_sort_ratio` – Token order-insensitive similarity  
   - `token_set_ratio` – Token set similarity ignoring duplicates  

#### **HMM Features**
- Sequence-based similarity using Hidden Markov Model.  

---

### 3️⃣ Model Training
- **Random Forest Classifier** for baseline predictions  
- **XGBoost** for final optimized predictions  

- ##  How to Run Locally

Follow these steps to clone and run the project on your system:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/duplicate-question-detector.git
cd duplicate-question-detector

python -m venv venv
# Activate the environment
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt

import nltk
nltk.download('stopwords')

streamlit run app.py


