from openai import OpenAI
import os

class AnswerGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        self.model = "gpt-4o"
    def generate_answer(self, condition, evidence):
        # Compose the structured prompt
        prompt = f"""
You are a medical assistant. Based on the provided condition and evidence, generate a concise first-aid response following these strict guidelines:

1. Start with "**Predicted Condition:**" and state the likely condition.
2. Under "**First Aid Steps:**", list 3 to 4 key first-aid steps in short bullet points.
3. Under "**Key Medicines:**", list up to 3 important medicines.
4. Under "**Citations:**", list 3 reliable medical sources.
5. The entire response must not exceed 250 words.
6. Do not add any unnecessary explanation or disclaimers. Avoid phrases like "it is recommended" or "always consult...".
7. Keep it short, precise, and professional.

Condition: {condition}

Evidence: {evidence}

Generate only the formatted response.
"""

        # Call OpenAI API
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a concise medical assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=400  # Hard limit to enforce short output
        )

        answer = response.choices[0].message.content.strip()
        return answer
