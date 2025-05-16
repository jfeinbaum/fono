from flask import Flask, render_template, jsonify, request, send_file, Response
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

    with open(path, 'rb') as f:
        data = f.read()

    # Build response manually with header
    response = Response(data, mimetype='audio/mpeg')
    response.headers['X-Audio-Path'] = path

    return response

if __name__ == "__main__":
    app.run(debug=True)
