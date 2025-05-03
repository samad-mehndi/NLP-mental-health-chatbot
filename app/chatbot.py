import os
import torch
import joblib
import pandas as pd
import torch.nn.functional as F
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from pathlib import Path

# Set HuggingFace to use offline mode explicitly
os.environ['TRANSFORMERS_OFFLINE'] = '1'
model_path = "mh_classifier_root"

tokenizer = AutoTokenizer.from_pretrained(str(model_path), local_files_only=True)
model = AutoModelForSequenceClassification.from_pretrained(str(model_path), local_files_only=True)
label_encoder = joblib.load("label_encoder.pkl")
intent_labels = label_encoder.classes_

# === Load dataset for response retrieval ===
df = pd.read_csv("app/data.csv")  # adjust path if needed
vectorizer = TfidfVectorizer(stop_words='english')
vectorizer.fit(df["questionText"])

# === Classify intent ===
def detect_intent(text: str) -> str:
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=1)
    pred = torch.argmax(probs, dim=1).item()
    return intent_labels[pred]

# === Retrieve best response based on topic + similarity ===
def retrieve_best_response(user_input, predicted_topic):
    topic_filtered = df[df["topic"] == predicted_topic]
    if topic_filtered.empty:
        return "I'm here to listen and help in any way I can."

    tfidf_topic = vectorizer.transform(topic_filtered["questionText"])
    user_vec = vectorizer.transform([user_input])
    cosine_sim = cosine_similarity(user_vec, tfidf_topic).flatten()

    best_idx = cosine_sim.argmax()
    return topic_filtered.iloc[best_idx]["answerText"]

# === Main response function ===
def generate_response(user_input: str) -> str:
    user_vec = vectorizer.transform([user_input])
    sims = cosine_similarity(user_vec, vectorizer.transform(df["questionText"]))
    best_idx = sims.argmax()
    best_score = sims[0][best_idx]
    
    if best_score < 0.2:
        return "I'm here to listen. Can you tell me more?"
    
    return df["answerText"].iloc[best_idx]
