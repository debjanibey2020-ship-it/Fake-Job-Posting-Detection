# Fake Job Posting Detection 🚨

Fake job postings are a growing problem in online recruitment platforms.  
This project uses **Natural Language Processing (NLP)** and **Deep Learning** to automatically detect whether a job posting is **real or fake** based on its content.

The system is deployed using **Streamlit** to provide an interactive and user-friendly web interface.

---

## 📌 Project Overview

The Fake Job Posting Detection system analyzes job descriptions and predicts their authenticity.  
It helps job seekers avoid scams by identifying suspicious or fraudulent job advertisements.

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Libraries & Frameworks:**
  - NumPy
  - Pandas
  - Scikit-learn
  - TensorFlow / Keras
  - Streamlit
- **Techniques Used:**
  - Natural Language Processing (NLP)
  - Text Vectorization
  - Deep Learning Classification

---

## ⚙️ How It Works

1. Job posting data is collected from a CSV dataset.
2. Text data is cleaned and preprocessed using NLP techniques.
3. A vectorizer converts text into numerical features.
4. A deep learning model is trained to classify job postings as **Real** or **Fake**.
5. The trained model is saved and used for prediction.
6. A Streamlit app allows users to input job descriptions and get instant results.

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/Fake-Job-Posting-Detection.git
