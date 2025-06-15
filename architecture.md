# Architecture Overview

## System Components

### 1️⃣ Ingestion Layer

- Loads ~60 curated medical knowledge snippets.
- Embeds them using OpenAI’s `text-embedding-ada-002`.
- Stores embeddings in persistent ChromaDB for semantic retrieval.

### 2️⃣ Condition Inference

- Uses OpenAI GPT-4o to classify user symptom input into one of 3 domains:
  - Diabetes
  - Cardiac
  - Renal

### 3️⃣ Hybrid Retrieval

- **Local Retrieval:** Semantic search on ChromaDB collection.
- **Web Retrieval:** Real-time web search using Serper.dev API.
- **Fusion:** Merges local & web results to form richer evidence context.

### 4️⃣ Answer Generation

- Uses GPT-4o to synthesize:
  - Predicted condition
  - First aid steps
  - Key medicines
  - Citations (max 250 words)
- Ensures output format consistency for downstream consumption.

### 5️⃣ API Layer

- FastAPI handles incoming requests (`/query`).
- Stateless orchestration of retriever, inferer, and generator modules.
- Pydantic models handle request validation.

### 6️⃣ Frontend (Separate React App)

- React app sends user queries to backend.
- Displays formatted markdown response with real-time feedback.

---

## Tech Stack

| Module     | Technology                      |
| ---------- | ------------------------------- |
| Embeddings | OpenAI `text-embedding-ada-002` |
| LLM        | OpenAI GPT-4o                   |
| Vector DB  | ChromaDB                        |
| Web Search | Serper.dev                      |
| Backend    | FastAPI                         |
| Frontend   | React.js                        |
| Testing    | Pytest                          |
| Deployment | Local / Cloud Compatible        |

---

## Notes

- ⚠ Educational use only.
- 🔐 All keys securely loaded via `.env` file.
