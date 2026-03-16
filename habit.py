import sqlite3
import argparse
from datetime import date

# connect database
conn = sqlite3.connect("habits.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TEXT,
    status INTEGER
)
""")

conn.commit()

# add habit
def add_habit(name):
    today = date.today().isoformat()
    cursor.execute(
        "INSERT INTO habits (name, date, status) VALUES (?, ?, ?)",
        (name, today, 0)
    )
    conn.commit()
    print(f"Habit '{name}' added for today.")

# mark habit done
def complete_habit(name):
    today = date.today().isoformat()
    cursor.execute(
        "UPDATE habits SET status = 1 WHERE name = ? AND date = ?",
        (name, today)
    )
    conn.commit()
    print(f"Habit '{name}' marked as completed.")

# show stats
def show_stats():
    cursor.execute("SELECT name, date, status FROM habits")
    rows = cursor.fetchall()

    if not rows:
        print("No habits found.")
        return

    for name, date_val, status in rows:
        status_text = "Done ✅" if status == 1 else "Pending ❌"
        print(f"{name} | {date_val} | {status_text}")

# CLI argument parser
parser = argparse.ArgumentParser(description="CLI Habit Tracker")

parser.add_argument("command", choices=["add", "done", "stats"])
parser.add_argument("--name", help="Name of the habit")

args = parser.parse_args()

if args.command == "add":
    add_habit(args.name)

elif args.command == "done":
    complete_habit(args.name)

elif args.command == "stats":
    show_stats()

conn.close()
