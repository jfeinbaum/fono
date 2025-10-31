
from pypdf import PdfReader
import os

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from model import initialize_fonz, initialize_edges, cached_audios

Base = declarative_base()

class Audio(Base):
    __tablename__ = 'audio'
    id = Column(Integer, primary_key=True)
    filepath = Column(String, nullable=False)
    sequence = Column(String, nullable=False)

    fonz = relationship("AudioFon", back_populates="audio")

class Fon(Base):
    __tablename__ = 'fon'
    id = Column(String, primary_key=True)
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



def get_db_dict():
    p = 'static/5-fonz/5-fonz answers.pdf'
    files = 'static/5-fonz/audio'

    reader = PdfReader(p)

    l = []

    for page in reader.pages:
        text = page.extract_text()
        l.extend(text.split('\n'))

    groups = []
    current_group = None
    for item in l:
        if item.startswith('Group'):
            current_group = []
            groups.append(current_group)
        elif current_group is not None:
            if ' ' not in item:
                current_group.append(item)

    groups = groups[:20]


    audio_dirs = []
    for afp in os.listdir(files):
        if afp.startswith('5'):
            audio_dirs.append(afp)

    audio_files = []

    for name in sorted(audio_dirs):
        afp = os.path.join(files, name)
        for fn in os.listdir(afp):
            if fn.startswith('5'):
                audio_files.append(os.path.join(afp, fn))

    audio_files = sorted(audio_files)
    audio_files = {os.path.basename(f): f for f in audio_files}

    path_to_answer = {}

    for i, group in enumerate(groups):
        group_no = i+1
        if group_no >= 10:
            group_zero = ''
        else:
            group_zero = '0'
        for j, item in enumerate(group):
            item_no = j + 1
            if item_no >= 10:
                item_zero = ''
            else:
                item_zero = '0'
            mp3_name = f'5-{group_zero}{group_no}-{item_zero}{item_no}.mp3'
            mp3_file = audio_files[mp3_name]

            path_to_answer[mp3_file] = item
    return path_to_answer


def create_database(name):

    engine = create_engine(f"sqlite:///{name}", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    data = cached_audios()
    for path, ans in data.items():
        session.add(Audio(filepath=path, sequence=ans))

    fonz = initialize_fonz()
    for fon in fonz:
        session.add(Fon(id=fon.id, symbol=fon.ipa))

    session.commit()


def database_exists(name):
    return os.path.exists(name)

def get_database_session(name):

    engine = create_engine(f"sqlite:///{name}")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def create_guess_table(session):
    class Guess(Base):
        __tablename__ = 'guesses'
        id = Column(Integer, primary_key=True)
        entry_id = Column(Integer, nullable=False)
        guess = Column(String, nullable=False)

    Base.metadata.create_all(session.bind)
    return Guess



def query_rows(session):

    audios = session.query(Audio).all()
    return audios

if __name__ == "__main__":
    create_database('fresh_database.db')