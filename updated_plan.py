import os
import google.generativeai as genai


API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)


def update_workout_plan(original_plan, feedback):

    prompt = f"""
You are FitBuddy, an AI fitness plan assistant.

Here is the user's original workout plan:

{original_plan}

User feedback:

{feedback}

Create an updated 7-day workout plan based on the
user's feedback.

Keep the plan structured and include:
- Warm-up
- Main workout
- Sets and repetitions or duration
- Rest
- Cool-down or recovery

Return only the updated workout plan.
"""

    if not API_KEY:
        return "Gemini API key is not configured."

    try:
        model = genai.GenerativeModel("gemini-3.8-flash")

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error updating workout plan: {str(e)}"