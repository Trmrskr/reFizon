#!/usr/bin/python3
"""This file contains the class for choices/options"""
from models.base_model import BaseModel
from models.question import Question
from sqlalchemy import Column, String, ForeignKey



class Choice(BaseModel):
    """The namespace for choice model"""

    question_id = Column(String(60), ForeignKey("questions.id"), nullable=False)
    option = Column(String(60), nullable=False)

