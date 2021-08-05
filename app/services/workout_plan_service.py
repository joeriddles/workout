from typing import Optional
from sqlalchemy.orm import Session

from app import models, db_models


def get_workout_plans(db: Session, skip: Optional[int]=None, limit: Optional[int]=0):
    skip = 0 if skip is None else skip
    limit = 10 if limit is None else limit
    return db.query(db_models.DbWorkoutPlan) \
        .offset(skip) \
        .limit(limit) \
        .all()


def get_workout_plan(db: Session, workout_plan_id: int):
    return db.query(db_models.DbWorkoutPlan) \
        .filter(db_models.DbWorkoutPlan.workout_plan_id == workout_plan_id) \
        .first()


def create_workout_plan(db: Session, workout_plan: models.CreateWorkoutPlan):
    db_workouts = [
        create_workout(db, workout)
        for workout
        in workout_plan.workouts
    ]

    workout_plan_data = workout_plan.dict()
    workout_plan_data.pop("workouts")

    db_workout_plan = db_models.DbWorkoutPlan(workouts=db_workouts, **workout_plan_data)
    db.add(db_workout_plan)
    db.commit()
    db.refresh(db_workout_plan)
    return db_workout_plan


def create_workout(db: Session, workout: models.CreateWorkout):
    db_workout = db_models.DbWorkout(**workout.dict())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout
