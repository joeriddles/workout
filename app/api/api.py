from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from app import dependencies, models
from app.services import workout_plan_service


router = APIRouter(prefix="/api")


@router.get("/{workout_plan_id}/",
    response_class=JSONResponse,
    response_model=models.WorkoutPlan
)
def get_workout_plan(workout_plan_id: int, db = Depends(dependencies.get_db)):
    workout_plan = workout_plan_service.get_workout_plan(db, workout_plan_id)
    if workout_plan is None:
        raise HTTPException(404, "Workout plan not found")
    return workout_plan


@router.post("/",
    response_class=JSONResponse,
    response_model=models.WorkoutPlan
)
def create_workout_plan(create_workout_plan: models.CreateWorkoutPlan, db = Depends(dependencies.get_db)):
    db_workout_plan = workout_plan_service.create_workout_plan(db, create_workout_plan)
    return db_workout_plan
