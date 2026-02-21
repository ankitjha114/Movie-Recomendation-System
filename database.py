import json
import os

DB_FILE = "users.json"

def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_users(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def register_user(name, email, mobile, age, genres):
    users = load_users()
    users[email] = {
        "name": name,
        "mobile": mobile,
        "age": age,
        "genres": genres,
        "watch_history": []
    }
    save_users(users)

def add_watch_history(email, movie):
    users = load_users()
    users[email]["watch_history"].append(movie)
    save_users(users)
