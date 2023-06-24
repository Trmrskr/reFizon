#!/usr/bin/python3
"""This file holds the model for Scores"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
import datetime

class Score(BaseModel, Base):
    """Class model of work"""

    __tablename__ = "scores"
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    score_id = Column(String(60), ForeignKey('scores.id'), nullable=False)
    exam_id = Column(String(60), ForeignKey('exams.id'), nullable=False)
    subject_id = Column(String(60), ForeignKey('subjects.id'), nullable=False)
    score = Column(Integer, nullable=False, default=0)
