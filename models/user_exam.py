#!/usr/bin/python3
import models
from sqlalchemy import Table, Column, String, ForeignKey
from models.base_model import Base


user_exam = Table("user_exam", Base.metadata,
                    Column("user_id", String(60),
                            ForeignKey('users.id'),
                            primary_key=True,
                            nullable=False),
                    Column("exam_id", String(60),
                            ForeignKey('exams.id'),
                            primary_key=True,
                            nullable=False))
