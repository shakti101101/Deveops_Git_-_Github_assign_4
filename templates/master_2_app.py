from flask import Flask, render_template,jsonify, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# -----------------------------
# MongoDB Connection
# -----------------------------
MONGO_URI = "mongodb+srv://shaktig101101_db_user:C1yoWqhkEj5muHcL@cluster0.sofmx8o.mongodb.net/"
  # Replace <db_password> with your actual password
  
# Connect to Atlas
client = MongoClient(MONGO_URI)

db = client["todo_db"]
collection = db["items"]

# -----------------------------
# Submit To-Do Item Route
# -----------------------------
@app.route("/submit_todo_item", methods=["POST"])
def submit_todo_item():
    try:
        item_name = request.form.get("itemName")
        item_description = request.form.get("itemDescription")


        todo_item = {
            "itemName": item_name,
            "itemDescription": item_description
        }

        collection.insert_one(todo_item)

        return jsonify({"message": "To-Do item added successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
