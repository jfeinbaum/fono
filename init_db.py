
from pypdf import PdfReader
import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    filepath = Column(String, nullable=False)
    answer = Column(String, nullable=False)

def get_db_dict():
    p = 'static/3-fonz/3-fonz answers.pdf'
    files = 'static/3-fonz/audio'

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

    groups = groups[:17]


    audio_dirs = []
    for afp in os.listdir(files):
        if afp.startswith('3'):
            audio_dirs.append(afp)

    audio_files = []

    for name in sorted(audio_dirs):
        afp = os.path.join(files, name)
        for fn in os.listdir(afp):
            if fn.startswith('3'):
                audio_files.append(os.path.join(afp, fn))

    audio_files = sorted(audio_files)
    audio_files = {os.path.basename(f): f for f in audio_files}

    path_to_answer = {}

    for i, group in enumerate(groups):
        group_no = i+1
        if group_no >= 10:
            zero = ''
        else:
            zero = '0'
        for j, item in enumerate(group):
            item_no = j + 1

            mp3_name = f'3-{zero}{group_no}-{item_no}.mp3'
            mp3_file = audio_files[mp3_name]

            path_to_answer[mp3_file] = item
    return path_to_answer


def create_database(name):

    engine = create_engine(f"sqlite:///{name}", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    data = get_db_dict()
    for path, ans in data.items():
        session.add(Entry(filepath=path, answer=ans))

    session.commit()

def database_exists(name):
    return os.path.exists(name)

def get_database_session(name):

    engine = create_engine(f"sqlite:///{name}")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def query_rows(session):

    entries = session.query(Entry).limit(5).all()
    return entries