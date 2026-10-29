from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import json
import os

app = Flask(__name__)

# ---------------- Frontend routes ----------------

@app.route("/")
def home():
    return "Flask Git Assignment"


@app.route("/api")
def api():
    with open("data.json") as f:
        return jsonify(json.load(f))

@app.route("/todo")
def todo():
    return render_template("todo.html")

# ---------------- Backend routes ----------------

if __name__ == "__main__":
    app.run(debug=True)
