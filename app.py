from flask import Flask, render_template, request, Response, jsonify, session
from init_db import create_database, database_exists, query_rows, get_database_session
from model import initialize_phonemes, initialize_edges
import random


app = Flask(__name__)
app.secret_key = 'test'

db_name = 'database.db'
if not database_exists(db_name):
    create_database(db_name)

db_session = get_database_session(db_name)
rows = query_rows(db_session)
phonemes = initialize_phonemes()
edges = initialize_edges()

current_answer = None


@app.route("/")
def index():
    return render_template("index.html", nodes=phonemes, edges=edges)

@app.route("/get-audio")
def get_audio():
    last = request.args.get('last')

    while True:
        choice = random.choice(rows)
        path = choice.filepath
        if path != last:
            break

    session['answer'] = choice.answer
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
        for p in phonemes:
            if p.ipa == char:
                id_seq += p.id
    answer = session.get('answer')
    print(f'guess: {id_seq} -- answer: {answer}')

    return jsonify({'correct': id_seq == answer})

if __name__ == "__main__":
    app.run(debug=False, port=8080)
