from __future__ import annotations
from enum import Enum

from pydantic import BaseModel


class WorkoutPlan(BaseModel):
    workout_plan_id: int
    restrictions: str
    client: str
    phase: str
    workouts: list[Workout]

    class Config:
        orm_mode = True


class Workout(BaseModel):
    workout_id: int
    session: int
    week: int
    category: WorkoutType
    sets: int
    reps: int
    notes: str

    class Config:
        orm_mode = True


class WorkoutType(str, Enum):
    Mobility = "Mobility"
    Squat = "Squat"
    ...

class CreateWorkoutPlan(BaseModel):
    restrictions: str
    client: str
    phase: str
    workouts: list[CreateWorkout]


class CreateWorkout(BaseModel):
    session: int
    week: int
    category: WorkoutType
    sets: int
    reps: int
    notes: str


WorkoutPlan.update_forward_refs()
Workout.update_forward_refs()
CreateWorkoutPlan.update_forward_refs()
CreateWorkout.update_forward_refs()
