import os
import google.generativeai as genai


API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)


def generate_nutrition_tip_with_flash(goal):

    prompt = f"""
You are FitBuddy, an AI fitness assistant.

Give one concise and practical nutrition or recovery tip
for the following fitness goal:

Fitness Goal: {goal}

The tip should be simple, safe and easy to follow.
"""

    if not API_KEY:
        return "Gemini API key is not configured."

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error generating nutrition tip: {str(e)}"