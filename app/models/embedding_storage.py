import numpy as np
import os

EMBEDDING_DIR = "embeddings"
os.makedirs(EMBEDDING_DIR, exist_ok=True)

def get_embedding_path(user_id: str) -> str:
    return os.path.join(EMBEDDING_DIR, f"{user_id}.npy")

def save_embedding(user_id: str, embedding: np.ndarray):
    """
    지정한 사용자 ID에 해당하는 음성 임베딩을 저장합니다.
    """
    path = get_embedding_path(user_id)
    np.save(path, embedding)

def load_embedding(user_id: str) -> np.ndarray:
    """
    저장된 임베딩을 불러옵니다.
    """
    path = get_embedding_path(user_id)
    if not os.path.exists(path):
        raise FileNotFoundError(f"사용자 '{user_id}'의 임베딩 파일이 존재하지 않습니다.")
    return np.load(path )