from resemblyzer import VoiceEncoder, preprocess_wav
from app.models.embedding_storage import save_embedding, load_embedding
import numpy as np
import os
import shutil
from fastapi import UploadFile
import uuid

UPLOAD_DIR = "voice_samples"
os.makedirs(UPLOAD_DIR, exist_ok=True)

VOICE_SAMPLE_PATH = os.path.join(UPLOAD_DIR, "voice_sample.wav")

encoder = VoiceEncoder()

async def process_and_store_embedding(file: UploadFile):
    with open(VOICE_SAMPLE_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        wav = preprocess_wav(VOICE_SAMPLE_PATH)
        embedding = encoder.embed_utterance(wav)
        save_embedding("default_user", embedding)


async def compare_embedding(file:UploadFile):
    temp_path = os.path.join(UPLOAD_DIR, "temp_input.wav")
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        wav = preprocess_wav(temp_path)
        new_embedding = encoder.embed_utterance(wav)

        existing_embedding = load_embedding("default_user")
        similarity = np.dot(existing_embedding, new_embedding)

        return similarity