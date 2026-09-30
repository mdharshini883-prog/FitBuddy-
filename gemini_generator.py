import os
import google.generativeai as genai


API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)


def generate_workout_gemini(name, age, weight, goal, intensity):
    prompt = f"""
Create a personalized 7-day fitness workout plan.

Name: {name}
Age: {age}
Weight: {weight} kg
Goal: {goal}
Intensity: {intensity}

For each day include:
1. Warm-up
2. Main workout
3. Cool-down or recovery

Keep the plan simple and structured.
"""

    if not API_KEY:
        return "Gemini API key is not configured yet."

    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)

    return response.text