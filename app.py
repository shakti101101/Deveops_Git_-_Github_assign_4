from flask import Flask, render_template,jsonify, request, redirect, url_for
from pymongo import MongoClient
import json
app = Flask(__name__)

# -----------------------------
# MongoDB Atlas Configuration
# -----------------------------
MONGO_URI = "mongodb+srv://shaktig101101_db_user:C1yoWqhkEj5muHcL@cluster0.sofmx8o.mongodb.net/"
  # Replace <db_password> with your actual password


# Connect to Atlas
client = MongoClient(MONGO_URI)

# Use the same database name as in URI
db = client["student_db"]  
collection = db["students"]  # collection name

@app.route("/")
def home():
    return render_template("index.html")

# -----------------------------
# Submit Form
# -----------------------------
@app.route("/submit", methods=["POST"])
def submit():
    try:
        student_data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "course": request.form["course"]
        }

        # Insert data into MongoDB
        collection.insert_one(student_data)

        return redirect(url_for("success"))
    except Exception as e:
        return render_template("index.html", error=str(e))

# -----------------------------
# Success Page
# -----------------------------
@app.route("/success")
def success():
    return render_template("success.html")

# -----------------------------
# 1. API Route
# -----------------------------

@app.route("/api")
def api():

    with open("data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)


# -----------------------------
# Start Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=False)
