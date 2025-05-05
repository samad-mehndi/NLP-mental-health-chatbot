import os
import torch
import joblib
import pandas as pd
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from pathlib import Path

# Initialize SentenceTransformer model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Set HuggingFace to use offline mode explicitly
os.environ['TRANSFORMERS_OFFLINE'] = '1'
model_path = "mh_classifier_root"

# Load intent classifier
tokenizer = AutoTokenizer.from_pretrained(str(model_path), local_files_only=True)
model = AutoModelForSequenceClassification.from_pretrained(str(model_path), local_files_only=True)
label_encoder = joblib.load("label_encoder.pkl")
intent_labels = label_encoder.classes_

# Load dataset with precomputed embeddings
base_dir = Path(__file__).resolve().parent
df = pd.read_pickle(base_dir / "data_with_embeddings1.pkl")

# Ensure embeddings are tensors (if needed)
df["embeddings"] = df["embeddings"].apply(lambda x: torch.tensor(x) if not isinstance(x, torch.Tensor) else x)

# Intent classifier
def detect_intent(text: str) -> str:
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=-1)
        intent_idx = torch.argmax(probs, dim=1).item()
    return intent_labels[intent_idx]

# Semantic response generator with intent filtering
def generate_response(user_input: str) -> str:
    user_embedding = embedder.encode(user_input, convert_to_tensor=True)

    # Detect top intent
    predicted_intent = detect_intent(user_input)
    filtered_df = df[df["topic"] == predicted_intent]

    if filtered_df.empty:
        return "I'm here to listen. Can you tell me more?"

    similarities = [util.pytorch_cos_sim(user_embedding, emb)[0][0].item() for emb in filtered_df["embeddings"]]
    best_idx = torch.tensor(similarities).argmax().item()
    best_score = similarities[best_idx]

    if best_score < 0.4:
        return "I'm here to listen. Can you tell me more?"

    return filtered_df.iloc[best_idx]["answerText"]