from flask import Blueprint, request, jsonify
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

loading_bp = Blueprint("loading_bp", __name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shivansh@1843",
    database="movie_recommender"
)
cursor = db.cursor(dictionary=True)


@loading_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json

    user_id = data["id"]       # Login Id
    name = data["name"]        # Full Name
    password = data["password"]

    # 🔍 Check if user already exists
    check_query = "SELECT * FROM users WHERE id=%s"
    cursor.execute(check_query, (user_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        return jsonify({"success": False, "message": "User already exists with this ID"}), 409

    hashed_password = generate_password_hash(password)

    query = "INSERT INTO users (id, name, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (user_id, name, hashed_password))
    db.commit()

    return jsonify({"success": True, "message": "Signup successful"})


@loading_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    user_id = data["id"]
    password = data["password"]

    query = "SELECT * FROM users WHERE id=%s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()

    if user and check_password_hash(user["password"], password):
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401