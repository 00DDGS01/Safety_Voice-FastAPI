import numpy as np
import os

EMBEDDING_DIR = "embeddings"
os.makedirs(EMBEDDING_DIR, exist_ok=True)

def save_embedding(user_id: str, embedding: np.ndarray):
    path = os.path.join(EMBEDDING_DIR, f"{user_id}.npy")
    np.save(path, embedding)

def load_embedding(user_id: str) -> np.ndarray:
    path = os.path.join(EMBEDDING_DIR, f"{user_id}.npy")
    return np.load(path)