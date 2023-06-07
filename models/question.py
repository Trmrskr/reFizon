#!/usr/bin/python3
"""This file holds the question class"""
from models import BaseModel, Question
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship



class Question(BaseModel):
    """The namespace of Question model"""

    __tablename__ = "questions"
    subject_id = Column(String(60), ForeignKey('subjects.id'), nullable=False)
    statement = Column(String(4096), nullable=False)
    year = Column(Integer, nullable=False)
    answer = Column(String(2048), nullable=False)
    choices = relationship("Choice", cascade='all, delete, delete-orphan', backref="questions")
