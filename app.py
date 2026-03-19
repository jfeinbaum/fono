from flask import Flask, render_template, request, Response, jsonify, session
from init_db import create_database, database_exists, query_rows, get_database_session
from model import initialize_fonz, initialize_edges
from db_utils import record_guess
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
import random



app = Flask(__name__)
app.secret_key = 'test'

db_name = 'database.db'
if not database_exists(db_name):
    create_database(db_name)


engine = create_engine(f'sqlite:///={db_name}')
SessionFactory = sessionmaker(bind=engine)
db_session = scoped_session(SessionFactory)
rows = query_rows(db_session)
fonz = initialize_fonz()
edges = initialize_edges()

current_answer = None


@app.route("/")
def index():
    return render_template("index.html", nodes=fonz, edges=edges)

@app.route("/get-audio")
def get_audio():
    last = request.args.get('last')

    while True:
        choice = random.choice(rows)
        path = choice.filepath
        if path != last:
            break

    session['answer'] = choice.sequence
    print('answer set to:', session.get('answer'))

    with open(path, 'rb') as f:
        data = f.read()

    response = Response(data, mimetype='audio/mpeg')
    response.headers['X-Audio-Path'] = path

    return response

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    seq = data['sequence']
    id_seq = ''
    for char in seq:
        for p in fonz:
            if p.ipa == char:
                id_seq += p.id
    answer = session.get('answer')
    print(f'guess: {id_seq} -- answer: {answer}')

    correct = id_seq == answer
    record_guess(db_session, id_seq, correct)

    return jsonify({'correct': correct})

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    app.run(debug=False, port=8080)
