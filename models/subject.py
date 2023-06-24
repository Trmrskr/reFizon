#!/usr/bin/python3
"""This file holds the class model Subject"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.exam import Exam



class Subject(BaseModel, Base):
    """The namespace of the class model"""

    __tablename__ = "subjects"
    exam_id = Column(String(60), ForeignKey("exams.id"), nullable=False)
    name = Column(String(64), nullable=False)
    faculty = Column(String(64), nullable=False)
