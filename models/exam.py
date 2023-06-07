#!/usr/bin/python3
"""This file holds the exam model"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from models.base_model import BaseModel
from models.user_exam import user_exam



class Exam(BaseModel):
    """The class namespace of exam"""
    

    __tablename__ = 'exams'
    name = Column(String(512), nullable=False)
    duration = Column(Integer, nullable=False, default=60)
    institution_name = Column(String(64), nullable=False)
    instructions = Column(String(4096), nullable=False)
    scores = relationship('Score', backref='exam', cascade='all, delete, delete-orphan')
    subject = relationship('Subject', backref='exam', cascade='all, delete, delete-orphan')
    user_exams = relationship("User", secondary=user_exam)
