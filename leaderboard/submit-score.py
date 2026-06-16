import requests
import json
import os

SERVER_URL  = "http://localhost:5000/score"
QUEUE_FILE  = "leaderboard/pending_scores.json"

def save_to_queue(name, time_seconds):
    """Save score locally if server is unreachable."""
    queue = []
    if os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE) as f:
            queue = json.load(f)
    queue.append({"name": name, "time": time_seconds})
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f)
    print(f"Score queued locally: {name} — {time_seconds}s")

def flush_queue():
    """Try to send any previously queued scores."""
    if not os.path.exists(QUEUE_FILE):
        return
    with open(QUEUE_FILE) as f:
        queue = json.load(f)
    remaining = []
    for entry in queue:
        success = submit_score(entry["name"], entry["time"])
        if not success:
            remaining.append(entry)
    with open(QUEUE_FILE, "w") as f:
        json.dump(remaining, f)

def submit_score(name, time_seconds):
    """Submit score to leaderboard, queue locally if server unreachable."""
    payload = {"name": name, "time": round(time_seconds, 2)}
    try:
        response = requests.post(SERVER_URL, json=payload, timeout=3)
        if response.status_code == 200:
            print(f"Score submitted: {name} — {time_seconds}s")
            flush_queue()  # send any previously failed scores too
            return True
        return False
    except Exception as e:
        print(f"Submission failed: {e}")
        save_to_queue(name, time_seconds)
        return False
