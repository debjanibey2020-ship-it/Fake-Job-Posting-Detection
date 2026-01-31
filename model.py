import pandas as pd
import numpy as np
import nltk
import pickle
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

nltk.download('stopwords')
from nltk.corpus import stopwords
import re
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    stop_words = set(stopwords.words('english'))
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text
df = pd.read_csv("fake_job_postings.csv", encoding="ISO-8859-1")


df['text'] = df['title'].fillna('') + ' ' + df['description'].fillna('')
df['text'] = df['text'].apply(clean_text)

X = df['text']
y = df['fraudulent']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train).toarray()
X_test_vec = vectorizer.transform(X_test).toarray()
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(X_train_vec.shape[1],)))
model.add(Dropout(0.3))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(1, activation='sigmoid'))

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
model.fit(
    X_train_vec,
    y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.1
)
model.save("fake_job_model.h5")

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model training completed and saved!")
