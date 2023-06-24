#!/usr/bin/python3
"""Import the storage engine to be used by the application"""


from models.engine.storage_engine import DBStorage
from models.user import User, user_exam
from models.exam import Exam
from models.subject import Subject
from models.score import Score
from models.question import Question
from models.choice import Choice

storage = DBStorage()
storage.reload()
