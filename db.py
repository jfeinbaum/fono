

from sqlalchemy import create_engine, MetaData, String, ForeignKey, Column, Integer, Table
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
    position = Column(Integer)  # optional

    audio = relationship("Audio", back_populates="fonz")
    fon = relationship("Fon", back_populates="audios")

# Connect to old and new databases
# old_engine = create_engine('sqlite:///database.db')
# new_engine = create_engine('sqlite:///new_database.db')
# Session = sessionmaker(bind=new_engine)

# Base.metadata.create_all(new_engine)

# old_meta = MetaData()
# old_meta.reflect(bind=old_engine)
# entries = old_meta.tables['entries']

# with Session() as session, old_engine.connect() as conn:
#     all_entries = conn.execute(entries.select()).fetchall()

#     fon_map = OrderedDict()
#     for row in all_entries:
#         for p in row.answer:
#             fon_map[p] = None
    
#     for f in fon_map:
#         fon_obj = Fon(symbol=f)
#         session.add(fon_obj)
#         fon_map[f] = fon_obj
    
#     session.flush()

#     for row in all_entries:
#         audio_obj = Audio(filepath=row.filepath, sequence=row.answer)
#         session.add(audio_obj)
#         session.flush()

#         for i, p in enumerate(row.answer):
#             fon_obj = fon_map[p]
#             audio_fon_obj = AudioFon(audio=audio_obj, fon=fon_obj, position=i)
#             session.add(audio_fon_obj)
    
#     session.commit()




