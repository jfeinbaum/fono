from flask import Flask, render_template, request, Response, jsonify
from init_db import create_database, database_exists, query_rows, get_database_session
from model import initialize_phonemes, initialize_edges
import random


app = Flask(__name__)

db_name = 'database.db'
if not database_exists(db_name):
    create_database(db_name)

session = get_database_session(db_name)
rows = query_rows(session)
phonemes = initialize_phonemes()
edges = initialize_edges()

current_answer = None


@app.route("/")
def index():
    return render_template("index.html", nodes=phonemes, edges=edges)

@app.route("/get-audio")
def get_audio():
    global current_answer
    last = request.args.get('last')

    while True:
        choice = random.choice(rows)
        path = choice.filepath
        if path != last:
            break

    current_answer = choice.answer
    print('answer set to:', current_answer)

    with open(path, 'rb') as f:
        data = f.read()

    response = Response(data, mimetype='audio/mpeg')
    response.headers['X-Audio-Path'] = path

    return response

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    seq = data['sequence']
    print(f'IPA guess: {"".join(seq)}')

    id_seq = ''
    for char in seq:
        for p in phonemes:
            if p.ipa == char:
                id_seq += p.id
            elif p.ipa_dot == char:
                id_seq += p.id_dot
    print(f'guess: {id_seq} -- answer: {current_answer}')

    return jsonify({'correct': id_seq == current_answer})

if __name__ == "__main__":
    app.run(debug=True)
