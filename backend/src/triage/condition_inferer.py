import os
from openai import OpenAI
from dotenv import dotenv_values

class ConditionInferer:
    def __init__(self):
        config = dotenv_values(os.path.join(os.path.dirname(__file__), "../../.env"))
        api_key = config.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in .env")
        self.client = OpenAI(api_key=api_key)

    def infer(self, symptoms):
        prompt = f"""
        You are a medical assistant. Given these symptoms, infer the most likely condition from Diabetes, Cardiac, Renal domains.
        Symptoms: {symptoms}
        Condition:
        """
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
