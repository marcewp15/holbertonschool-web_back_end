#!/usr/bin/env python3
""" User authentication service """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import User


from user import Base


class DB:
    """ DB Class: database """
    def __init__(self):
        """ Constructor method """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ create session """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session


    def add_user(self, email: str, hashed_password: str) -> User:
        """ add_user method """
        add_u = User(email = email, hashed_password = hashed_password)
        self._session.add(add_u)
        self._session.commit()
        return add_u
