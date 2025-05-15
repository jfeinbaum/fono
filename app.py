from flask import Flask, render_template, jsonify, request
from init_db import create_database, database_exists, query_rows, get_database_session


app = Flask(__name__)

db_name = 'database.db'
if not database_exists(db_name):
    create_database(db_name)

session = get_database_session(db_name)
query_rows(session)



nodes = [
    {"id": "Y", "x": 300, "y": 100, "dot": False},
    {"id": "I", "x": 350, "y": 135, "dot": False},
    {"id": "⋂", "x": 400, "y": 175, "dot": False},
    {"id": "Ǝ", "x": 450, "y": 215, "dot": False},
    {"id": "Ɐ", "x": 500, "y": 250, "dot": False},
    {"id": "A", "x": 500, "y": 100, "dot": False},
    {"id": "E", "x": 450, "y": 135, "dot": False},
    {"id": "O", "x": 350, "y": 215, "dot": False},
    {"id": "U", "x": 300, "y": 250, "dot": False},
    {"id": "L", "x": 400, "y": 100, "dot": False},
    {"id": "R", "x": 400, "y": 250, "dot": False},
    {"id": "P", "x": 600, "y": 100, "dot": True},
    {"id": "T", "x": 650, "y": 100, "dot": True},
    {"id": "K", "x": 700, "y": 100, "dot": True},
    {"id": "B", "x": 600, "y": 175, "dot": True},
    {"id": "D", "x": 650, "y": 175, "dot": True},
    {"id": "G", "x": 700, "y": 175, "dot": True},
    {"id": "M", "x": 600, "y": 250, "dot": True},
    {"id": "N", "x": 650, "y": 250, "dot": True},
    {"id": "Ŋ", "x": 700, "y": 250, "dot": True},
    {"id": "H", "x": 875, "y": 40, "dot": False},
    {"id": "F", "x": 800, "y": 100, "dot": False},
    {"id": "Φ", "x": 850, "y": 100, "dot": False},
    {"id": "S", "x": 900, "y": 100, "dot": False},
    {"id": "Ƨ", "x": 950, "y": 100, "dot": False},
    {"id": "V", "x": 800, "y": 175, "dot": False},
    {"id": "θ", "x": 850, "y": 175, "dot": False},
    {"id": "Z", "x": 900, "y": 175, "dot": False},
    {"id": "J", "x": 950, "y": 175, "dot": False}
]

edges = [
    ("Y", "I"),
    ("I", "⋂"),
    ("⋂", "Ǝ"),
    ("Ǝ", "Ɐ"),
    ("A", "E"),
    ("E", "⋂"),
    ("⋂", "O"),
    ("O", "U"),
    ("L", "⋂"),
    ("⋂", "R"),
    ("Ɐ", "M"),
    ("P", "T"),
    ("T", "K"),
    ("B", "M"),
    ("D", "N"),
    ("G", "Ŋ"),
    ("B", "D"),
    ("D", "G"),
    ("M", "N"),
    ("N", "Ŋ"),
    ("Ŋ", "V"),
    ("F", "Φ"),
    ("Φ", "S"),
    ("S", "Ƨ"),
    ("V", "θ"),
    ("θ", "Z"),
    ("Z", "J"),
]

dot_map = {
    "P": "Ṗ",
    "T": "Ṫ",
    "K": "K̇",
    "B": "Ḃ",
    "D": "Ḋ",
    "G": "Ġ",
    "M": "Ṁ",
    "N": "Ṅ",
    "Ŋ": "Ŋ̇"
}

class NodeTracker:
    def __init__(self):
        self.clicked_nodes = []

    def add_node(self, node_id):
        self.clicked_nodes.append(node_id)

    def get_clicked_nodes(self):
        return self.clicked_nodes

node_tracker = NodeTracker()

@app.route('/api/node_click', methods=['POST'])
def node_click():
    data = request.json
    node_id = data.get('node_id')

    node_tracker.add_node(node_id)

    return jsonify({
        'message': f'Node {node_id} clicked!',
        'clicked_nodes': node_tracker.get_clicked_nodes(),
        'status': 'success'
    })

@app.route('/api/node_dot_click', methods=['POST'])
def node_dot_click():
    data = request.json
    node_id = data.get('node_id')


    node_id_with_dot = dot_map[node_id]
    node_tracker.add_node(node_id_with_dot)
    return jsonify({
        'message': f'Node {node_id} dot ({node_id_with_dot}) clicked!',
        'clicked_nodes': node_tracker.get_clicked_nodes(),
        'status': 'success'
    })

@app.route("/")
def index():
    node_tracker.__init__()
    return render_template("index.html", nodes=nodes, edges=edges)

if __name__ == "__main__":
    app.run(debug=True)
