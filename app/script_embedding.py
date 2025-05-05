import time
import pandas as pd
from pathlib import Path
from sentence_transformers import SentenceTransformer

# Start timing
start_time = time.time()

# Load dataset
base_dir = Path(__file__).resolve().parent
df = pd.read_csv(base_dir / "data.csv")
df = df.dropna(subset=['questionText', 'answerText', 'topic'])
print(f"Dataset loaded in {time.time() - start_time:.2f} seconds")

# Load sentence transformer model
embedder = SentenceTransformer("all-MiniLM-L6-v2")
print(f"Model loaded in {time.time() - start_time:.2f} seconds")

# Compute embeddings in batches
questions = df["questionText"].tolist()
embeddings = embedder.encode(questions, batch_size=32, convert_to_tensor=True)
print(f"Embeddings computed in {time.time() - start_time:.2f} seconds")

# Add embeddings to the dataframe (convert tensors to lists)
df["embeddings"] = [embedding.tolist() for embedding in embeddings]

# Save the dataframe with embeddings
df.to_pickle(base_dir / "data_with_embeddings1.pkl")
print(f"Data saved in {time.time() - start_time:.2f} seconds")