import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

favorites_characters = Table('favorites_characters', Base.metadata,
                             Column('user_id', ForeignKey(
                                 'user.id'), primary_key=True),
                             Column('character_id', ForeignKey(
                                 'character.id'), primary_key=True)
                             )

# Association Table for the many-to-many relationship between User and Planet
favorites_planets = Table('favorites_planets', Base.metadata,
                          Column('user_id', ForeignKey(
                              'user.id'), primary_key=True),
                          Column('planet_id', ForeignKey(
                              'planet.id'), primary_key=True)
                          )


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    favorite_characters = relationship(
        'Character', secondary=favorites_characters, back_populates='favorited_by')
    favorite_planets = relationship(
        'Planet', secondary=favorites_planets, back_populates='favorited_by')


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorited_by = relationship(
        'User', secondary=favorites_characters, back_populates='favorite_characters')


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorited_by = relationship(
        'User', secondary=favorites_planets, back_populates='favorite_planets')


class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
