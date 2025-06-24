import os
import requests
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dotenv import load_dotenv

class HybridRetriever:
    def __init__(self, chroma_path="./chroma_db"):
        load_dotenv()
        openai_key = os.getenv("OPENAI_API_KEY")
        self.serper_key = os.getenv("SERPER_API_KEY")
        self.client = chromadb.PersistentClient(path=chroma_path)
        self.collection = self.client.get_or_create_collection(
            name="medical_snippets",
            embedding_function=OpenAIEmbeddingFunction(api_key=openai_key, model_name="text-embedding-ada-002")
        )

    def local_search(self, query, top_k=3):
        results = self.collection.query(query_texts=[query], n_results=top_k)
        return results['documents'][0]

    def serper_search(self, query):
        url = "https://google.serper.dev/search"  
        headers = {"X-API-KEY": self.serper_key}
        data = {"q": query}

        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()

            try:
                json_data = response.json()
            except Exception as json_err:
                print("Failed to parse Serper response as JSON.")
                print("Response text:", response.text)
                return []

            if 'organic' in json_data:
                return [item['snippet'] for item in json_data['organic'][:3]]
            return []
        except requests.exceptions.RequestException as req_err:
            print("Serper request failed:", req_err)
            return []

    def retrieve(self, query):
        local_results = self.local_search(query)
        web_results = self.serper_search(query)
        fused_results = local_results + web_results
        return fused_results
