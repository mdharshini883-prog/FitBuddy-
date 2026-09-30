from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.gemini_generator import generate_workout_gemini
from app.gemini_flash_generator import generate_nutrition_tip_with_flash
from app.updated_plan import update_workout_plan

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@router.post("/generate-workout", response_class=HTMLResponse)
async def generate_workout(
    request: Request,
    name: str = Form(...),
    user_id: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...)
):
    workout_plan = generate_workout_gemini(
        name, age, weight, goal, intensity
    )

    nutrition_tip = generate_nutrition_tip_with_flash(goal)

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "request": request,
            "name": name,
            "user_id": user_id,
            "age": age,
            "weight": weight,
            "goal": goal,
            "intensity": intensity,
            "workout_plan": workout_plan,
            "nutrition_tip": nutrition_tip
        }
    )


@router.post("/submit-feedback", response_class=HTMLResponse)
async def submit_feedback(
    request: Request,
    original_plan: str = Form(...),
    feedback: str = Form(...)
):
    updated_plan = update_workout_plan(
        original_plan,
        feedback
    )

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "request": request,
            "name": "User",
            "user_id": "",
            "age": "",
            "weight": "",
            "goal": "",
            "intensity": "",
            "workout_plan": updated_plan,
            "nutrition_tip": "Your workout plan has been updated based on your feedback."
        }
    )