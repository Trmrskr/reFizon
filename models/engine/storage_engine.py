#!/usr/bin/python3

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("REFIZON_MYSQL_USER")
        passwd = getenv("REFIZON_MYSQL_PWD")
        db = getenv("REFIZON_MYSQL_DB")
        host = getenv("REFIZON_MYSQL_HOST")
        env = getenv("REFIZON_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}'.format(user, passwd, host, db), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)
