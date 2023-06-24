#!/usr/bin/python3
"""This file contains the class for choices/options"""
from models.base_model import BaseModel, Base
from models.question import Question
from sqlalchemy import Column, String, ForeignKey



class Choice(BaseModel, Base):
    """The namespace for choice model"""

    __tablename__ = "choices"
    question_id = Column(String(60), ForeignKey("questions.id"), nullable=False)
    option = Column(String(60), nullable=False)

