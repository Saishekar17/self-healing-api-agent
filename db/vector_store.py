import faiss
import pickle
import os
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
DIM = 384
STORE_PATH = "data/fixes.pkl"

model = SentenceTransformer(MODEL_NAME)

index = faiss.IndexFlatL2(DIM)
memory = []

def load_memory():
    global index, memory
    if os.path.exists(STORE_PATH):
        try:
            with open(STORE_PATH, "rb") as f:
                index, memory = pickle.load(f)
        except:
            index = faiss.IndexFlatL2(DIM)
            memory = []

def save_memory():
    os.makedirs("data", exist_ok=True)
    with open(STORE_PATH, "wb") as f:
        pickle.dump((index, memory), f)

def add_to_memory(error, analysis, fix):
    record = {
        "error": error,
        "analysis": analysis,
        "fix": fix
    }

    text = f"{error} {analysis} {fix}"
    embedding = model.encode([text])
    embedding = np.array(embedding).astype("float32")

    index.add(embedding)
    memory.append(record)

    save_memory()

def search_similar(query, k=3):
    if len(memory) == 0:
        return []

    embedding = model.encode([query])
    embedding = np.array(embedding).astype("float32")

    D, I = index.search(embedding, k)

    results = []
    for idx in I[0]:
        if idx < len(memory):
            item = memory[idx]
            results.append(f"""
Error: {item['error']}
Fix: {item['fix']}
""")

    return results