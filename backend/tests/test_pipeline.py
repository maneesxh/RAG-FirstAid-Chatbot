import os
import pytest
from src.triage.condition_inferer import ConditionInferer
from src.retriever.hybrid_retriever import HybridRetriever
from src.generator.answer_generator import AnswerGenerator

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Fixtures to initialize modules once
@pytest.fixture(scope="module")
def triage():
    return ConditionInferer()

@pytest.fixture(scope="module")
def retriever():
    return HybridRetriever()

@pytest.fixture(scope="module")
def generator():
    return AnswerGenerator()

def test_condition_inference(triage):
    symptoms = "Crushing chest pain shooting down my left arm"
    condition = triage.infer(symptoms)
    assert "Myocardial Infarction" in condition or "Heart Attack" in condition

def test_retriever_returns_data(retriever):
    query = "hypoglycemia symptoms shaking and sweating"
    results = retriever.retrieve(query)
    assert isinstance(results, list)
    assert len(results) > 0

def test_answer_generation(generator):
    condition = "Hypoglycemia"
    evidence = [
        "Symptoms include sweating, shakiness, and low blood sugar.",
        "Treatment involves providing fast-acting carbohydrates."
    ]
    answer = generator.generate_answer(condition, evidence)
    assert "First aid steps" in answer or "first-aid steps" in answer
    assert len(answer) < 1000  # check response is reasonable size

def test_pipeline_end_to_end(triage, retriever, generator):
    user_input = "My diabetic father just became unconscious; we think his sugar crashed."
    condition = triage.infer(user_input)
    evidence = retriever.retrieve(user_input)
    answer = generator.generate_answer(condition, evidence)
    assert condition != ""
    assert len(evidence) > 0
    assert "First aid" in answer or "first-aid" in answer
