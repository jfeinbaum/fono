

from sqlalchemy import create_engine, MetaData, String, ForeignKey, Column, Integer, Table, update
from sqlalchemy.orm import relationship, declarative_base
from collections import OrderedDict
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Audio(Base):
    __tablename__ = 'audio'
    id = Column(Integer, primary_key=True)
    filepath = Column(String, nullable=False)
    sequence = Column(String, nullable=False)

    fonz = relationship("AudioFon", back_populates="audio")

class Fon(Base):
    __tablename__ = 'fon'
    id = Column(Integer, primary_key=True)
    symbol = Column(String, unique=True, nullable=False)
    correct_guesses = Column(Integer, default=0)
    total_guesses = Column(Integer, default=0)

    audios = relationship("AudioFon", back_populates="fon")

class AudioFon(Base):
    __tablename__ = 'audio_fon'
    id = Column(Integer, primary_key=True)
    audio_id = Column(Integer, ForeignKey('audio.id'))
    fon_id = Column(Integer, ForeignKey('fon.id'))
    position = Column(Integer)

    audio = relationship("Audio", back_populates="fonz")
    fon = relationship("Fon", back_populates="audios")


def record_guess(session, sequence, correct):
    symbols = list(sequence)
    fons = session.query(Fon).filter(Fon.symbol.in_(symbols)).all()

    for fon in fons:
        fon.total_guesses += 1
        if correct:
            fon.correct_guesses += 1

    session.commit()
