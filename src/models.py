import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable = False)
    last_name = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    user = relationship('User')


class Media(Base):
    __tablename__ ='media'
    id = Column(Integer, primary_key = True)
    media_type = Column(String(100), nullable = False)
    url = Column(String(300), nullable = False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable = False)
    post = relationship('Post')

class Comment (Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True)
    text = Column(String(300), nullable = False)
    author = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')


class Followers (Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key = True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')







## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
