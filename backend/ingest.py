import os
from src.ingestion.embedder import Embedder

if __name__ == "__main__":
    csv_path = "data/medical_snippets.csv"
    if not os.path.exists(csv_path):
        print(f"CSV file not found at {csv_path}")
    else:
        embedder = Embedder()
        embedder.embed_corpus(csv_path)
