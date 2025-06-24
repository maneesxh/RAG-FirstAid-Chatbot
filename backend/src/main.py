import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.triage.condition_inferer import ConditionInferer
from src.generator.answer_generator import AnswerGenerator
from src.retriever.hybrid_retriever import HybridRetriever
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

retriever = HybridRetriever()
triage = ConditionInferer()
generator = AnswerGenerator()

class QueryRequest(BaseModel):
    user_input: str

@app.post("/query")
def process_query(request: QueryRequest):
    try:
        condition = triage.infer(request.user_input)
        evidence = retriever.retrieve(request.user_input)
        answer = generator.generate_answer(condition, evidence)
        return {"condition": condition, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
