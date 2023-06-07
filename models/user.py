#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models.user_exam import user_exam
import models



class User(BaseModel):
    """
    This is the class for user
    Attributes:
        first_name: User first name
        surname: user surname
        email: User email address
        phone_number: the users phone number
        password: User password
        admin: a boolean value, true or false
    """

    __tablename__ = "users"
    first_name = Column(String(128), nullable=False)
    surname = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    phone_number = Column(String(11), nullable=False)
    password = Column(String(20), nullable=False)
    admin = Column(Boolean, nullable=False, default=False)
    scores = relationship('Score', backref='user', cascade='all, delete, delete-orphan')
    exams = relationship('Exam', secondary=user_exam, viewonly=False, back_populates="user_exam")

