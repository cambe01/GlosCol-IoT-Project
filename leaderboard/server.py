from flask import Flask, request, jsonify, render_template_string
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB = "scores.db"

# Create the database table if it doesn't exist
def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name    TEXT,
            time    REAL,
            date    TEXT
        )
    """)
    conn.commit()
    conn.close()

# Leaderboard HTML page
LEADERBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Hackbox Leaderboard</title>
    <meta http-equiv="refresh" content="5">  <!-- auto-refresh every 5 seconds -->
    <style>
        body {
            background: #0a0a0a;
            color: #00ff88;
            font-family: monospace;
            text-align: center;
            padding: 40px;
        }
        h1 { font-size: 3em; margin-bottom: 10px; }
        table {
            margin: 0 auto;
            border-collapse: collapse;
            font-size: 1.8em;
            width: 80%;
        }
        th {
            border-bottom: 2px solid #00ff88;
            padding: 10px 20px;
        }
        td { padding: 10px 20px; }
        tr:nth-child(1) td { color: gold; font-size: 1.2em; }
        tr:nth-child(2) td { color: silver; }
        tr:nth-child(3) td { color: #cd7f32; }
    </style>
</head>
<body>
    <h1>🔐 HACKBOX LEADERBOARD</h1>
    <table>
        <tr><th>#</th><th>Name</th><th>Time</th></tr>
        {% for i, row in scores %}
        <tr>
            <td>{{ i }}</td>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}s</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

# Route: show leaderboard
@app.route("/leaderboard")
def leaderboard():
    conn = sqlite3.connect(DB)
    scores = conn.execute(
        "SELECT name, ROUND(time, 1) FROM scores ORDER BY time ASC LIMIT 10"
    ).fetchall()
    conn.close()
    return render_template_string(
        LEADERBOARD_HTML,
        scores=enumerate(scores, start=1)
    )

# Route: receive a new score from the game Pi
@app.route("/score", methods=["POST"])
def add_score():
    data = request.get_json()
    name = data.get("name", "Anonymous")
    time = data.get("time", 0)
    conn = sqlite3.connect(DB)
    conn.execute(
        "INSERT INTO scores (name, time, date) VALUES (?, ?, ?)",
        (name, time, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()
    return jsonify({"status": "ok"})

# Route: reset all scores (useful between sessions)
@app.route("/reset", methods=["POST"])
def reset():
    conn = sqlite3.connect(DB)
    conn.execute("DELETE FROM scores")
    conn.commit()
    conn.close()
    return jsonify({"status": "scores cleared"})

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)
