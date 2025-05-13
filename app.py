from flask import Flask, render_template

app = Flask(__name__)

nodes = [

    {"id": "Y", "x": 100, "y": 100},
    {"id": "I", "x": 150, "y": 135},
    {"id": "⋂", "x": 200, "y": 175},
    {"id": "Ǝ", "x": 250, "y": 215},
    {"id": "Ɐ", "x": 300, "y": 250},
    {"id": "A", "x": 300, "y": 100},
    {"id": "E", "x": 250, "y": 135},
    {"id": "O", "x": 150, "y": 215},
    {"id": "U", "x": 100, "y": 250},
    {"id": "L", "x": 200, "y": 100},
    {"id": "R", "x": 200, "y": 250},


    {"id": "P", "x": 400, "y": 100},
    {"id": "T", "x": 450, "y": 100},
    {"id": "K", "x": 500, "y": 100},

    {"id": "B", "x": 400, "y": 175},
    {"id": "D", "x": 450, "y": 175},
    {"id": "G", "x": 500, "y": 175},
    {"id": "M", "x": 400, "y": 250},
    {"id": "N", "x": 450, "y": 250},
    {"id": "Ŋ", "x": 500, "y": 250},

    {"id": "H", "x": 675, "y": 25},
    {"id": "F", "x": 600, "y": 100},
    {"id": "Φ", "x": 650, "y": 100},
    {"id": "S", "x": 700, "y": 100},
    {"id": "Ƨ", "x": 750, "y": 100},
    {"id": "V", "x": 600, "y": 175},
    {"id": "θ", "x": 650, "y": 175},
    {"id": "Z", "x": 700, "y": 175},
    {"id": "J", "x": 750, "y": 175},
]

edges = [
    {"nodeA": "Y", "nodeB": "I"},
    {"nodeA": "I", "nodeB": "⋂"},
    {"nodeA": "⋂", "nodeB": "Ǝ"},
    {"nodeA": "Ǝ", "nodeB": "Ɐ"},

    {"nodeA": "A", "nodeB": "E"},
    {"nodeA": "E", "nodeB": "⋂"},
    {"nodeA": "⋂", "nodeB": "O"},
    {"nodeA": "O", "nodeB": "U"},

    {"nodeA": "L", "nodeB": "⋂"},
    {"nodeA": "⋂", "nodeB": "R"},
]

edges += [
    {"nodeA": "Ɐ", "nodeB": "M"},

    {"nodeA": "P", "nodeB": "T"},
    {"nodeA": "T", "nodeB": "K"},

    {"nodeA": "B", "nodeB": "M"},
    {"nodeA": "D", "nodeB": "N"},
    {"nodeA": "G", "nodeB": "Ŋ"},

    {"nodeA": "B", "nodeB": "D"},
    {"nodeA": "D", "nodeB": "G"},
    {"nodeA": "M", "nodeB": "N"},
    {"nodeA": "N", "nodeB": "Ŋ"},

    {"nodeA": "Ŋ", "nodeB": "V"},
]

edges += [
    {"nodeA": "F", "nodeB": "Φ"},
    {"nodeA": "Φ", "nodeB": "S"},
    {"nodeA": "S", "nodeB": "Ƨ"},

    {"nodeA": "V", "nodeB": "θ"},
    {"nodeA": "θ", "nodeB": "Z"},
    {"nodeA": "Z", "nodeB": "J"},


]



@app.route("/")
def index():
    return render_template("index.html", nodes=nodes, edges=edges)

if __name__ == "__main__":
    app.run(debug=True)
