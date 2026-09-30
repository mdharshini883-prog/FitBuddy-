import os
import google.generativeai as genai


# Gemini API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_nutrition_tip(goal):
    prompt = f"""
    Give one short, practical nutrition or recovery tip
    for a person whose fitness goal is: {goal}.

    Keep the answer simple and actionable.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)

    return response.text