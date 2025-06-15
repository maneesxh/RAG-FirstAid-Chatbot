import os
import pandas as pd
import chromadb
from openai import OpenAI
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dotenv import load_dotenv

class Embedder:
    def __init__(self, chroma_path="./chroma_db"):
        load_dotenv()
        openai_key = os.getenv("OPENAI_API_KEY")
        self.client = chromadb.PersistentClient(path=chroma_path)
        self.embedding_fn = OpenAIEmbeddingFunction(api_key=openai_key, model_name="text-embedding-ada-002")
        self.collection = self.client.get_or_create_collection(
            name="medical_snippets",
            embedding_function=self.embedding_fn
        )

    def embed_corpus(self, csv_file):
        df = pd.read_csv(csv_file)
        snippets = df['snippet'].tolist()
        for i, snippet in enumerate(snippets):
            self.collection.add(documents=[snippet], ids=[str(i)])
        print("Embedding completed and stored.")
