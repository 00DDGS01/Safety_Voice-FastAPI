from resemblyzer import VoiceEncoder, preprocess_wav
from app.models.embedding_storage import save_embedding, load_embedding
import numpy as np
import os
import shutil
from fastapi import UploadFile

UPLOAD_DIR = "voice_samples"
os.makedirs(UPLOAD_DIR, exist_ok=True)

encoder = VoiceEncoder()

async def process_and_store_embedding(file: UploadFile, user_id: str):

    user_sample_path = os.path.join(UPLOAD_DIR, f"{user_id}_voice.wav")

    with open(user_sample_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        wav = preprocess_wav(user_sample_path)
        embedding = encoder.embed_utterance(wav)
        save_embedding(user_id, embedding)


async def compare_embedding(file: UploadFile, user_id: str):
    temp_path = os.path.join(UPLOAD_DIR, f"{user_id}_temp.wav")

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    wav = preprocess_wav(temp_path)
    new_embedding = encoder.embed_utterance(wav)

    existing_embedding = load_embedding(user_id)
    similarity = np.dot(existing_embedding, new_embedding)

    return similarity