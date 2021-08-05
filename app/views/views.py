from app.models.models import CreateWorkoutPlan
from typing import Optional
from fastapi import APIRouter, Request
from fastapi.param_functions import Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app import dependencies
from app.services import workout_plan_service


router = APIRouter(default_response_class=Jinja2Templates)

templates = Jinja2Templates(directory="templates")


@router.get("/")
def workout_plans(
    request: Request,
    db=Depends(dependencies.get_db),
    skip: Optional[int] = None,
    limit: Optional[int] = None
):
    workout_plans = workout_plan_service.get_workout_plans(db, skip=skip, limit=limit)
    return templates.TemplateResponse("workout_plans.html", {"request": request, "workout_plans": workout_plans })


@router.get("/create/")
def create_workout_plan(request: Request):
    return templates.TemplateResponse("create_workout_plan.html", {"request": request })


@router.post("/create/submit/")
def create_workout_plan_submit(
    restrictions: str = Form(...),
    client: str = Form(...),
    phase: str = Form(...),
    db = Depends(dependencies.get_db),
):
    workout_plan = CreateWorkoutPlan(
        restrictions = restrictions,
        client = client,
        phase = phase,
        workouts = []
    )
    db_workout_plan = workout_plan_service.create_workout_plan(db, workout_plan)
    return RedirectResponse(f"/{db_workout_plan.workout_plan_id}/", status_code=303)


@router.get("/{workout_plan_id}/")
def workout_plan(
    request: Request,
    workout_plan_id: int,
    db=Depends(dependencies.get_db),
):
    workout_plan = workout_plan_service.get_workout_plan(db, workout_plan_id)
    return templates.TemplateResponse("workout_plan.html", {"request": request, "workout_plan": workout_plan })
