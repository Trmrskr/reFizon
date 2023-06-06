#!/usr/bin/python3
"""This file holds the exam model"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer

class Exam(BaseModel):
    """The class namespace of exam"""
    
    __tablename__ = 'exam'
    name = Column(String(512), nullable=False)
    duration = Column(Integer, nullable=False, default=60)
    institution_name = Column(String(64), nullable=False)
    instructions = Column(String(4096), nullable=False)
    scores = relationship('scores', backref='exam', cascade='all, delete, delete-orphan')
    subject = relationship('subjects', backref='exam', cascade='all, delete, delete-orphan')
    user_exam = relationship("users", secondary=user_exam)
