from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class DbWorkoutPlan(Base):
    __tablename__ = "workout_plans"

    workout_plan_id = Column(Integer, primary_key=True)
    restrictions = Column(String)
    client = Column(String)
    phase = Column(String)
    workouts = relationship("DbWorkout")


class DbWorkout(Base):
    __tablename__ = "workouts"

    workout_id = Column(Integer, primary_key=True)
    session = Column(Integer)
    week = Column(Integer)
    category = Column(String)
    workout = Column(String)
    sets = Column(Integer)
    reps = Column(Integer)
    notes = Column(Integer)

    workout_plan_id = Column(Integer, ForeignKey("workout_plans.workout_plan_id"))
    workout_plan = relationship("DbWorkoutPlan", back_populates="workouts")
