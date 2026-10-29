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


# ---------------- Backend routes ----------------
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = client["todo_db"]
todo_collection = db["todos"]


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.get_json(silent=True) or request.form
    item_name = data.get("itemName")
    item_description = data.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({"error": "itemName and itemDescription required"}), 400

    todo_collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })
    return jsonify({"message": "To-Do item saved"}), 201

if __name__ == "__main__":
    app.run(debug=True)
