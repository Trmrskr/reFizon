#!/usr/bin/python3
""" The module manages the storage engine of the application"""

from os import getenv
from models.base_model import Base
from models.user import User
from models.exam import Exam
from models.score import Score
from models.subject import Subject
from models.question import Question
from models.choice import Choice
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base

class DBStorage:
    """ This manages the storage engine"""
    __engine = None
    __session = None

    def __init__(self):
#        user = getenv("REFIZON_MYSQL_USER")
#        passwd = getenv("REFIZON_MYSQL_PWD")
#        db = getenv("REFIZON_MYSQL_DB")
#        host = getenv("REFIZON_MYSQL_HOST")
#        env = getenv("REFIZON_ENV")
        user = "refizon_test"
        passwd = "refizon_test_pwd"
        db = "refizon_db"
        host = "localhost"

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                        .format(user, passwd, host, db),
                                        pool_pre_ping=True)

#        if env == "test":
        Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            classList = [User, Exam, Score, Subject, Question, Choice]
            for item in classList:
                query = self.__session.query(item)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """add a new element in the table"""

        self.__session.add(obj)

    def save(self):
        """Save changes to database"""

        self.__session.commit()

    def delete(self, obj=None):
        """Delete an element in the table"""

        if obj:
            self.session.delete(obj)

    def reload(self):
        """Load tables to database"""

        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """Closes the database session"""

        self.__session.close()
