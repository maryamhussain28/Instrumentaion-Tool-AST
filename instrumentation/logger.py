import json
import time

LOG_FILE = "instrumentation.log"

def log_event(data):
    data["timestamp"] = time.time()

    print(data)   # 👈 ADD THIS LINE

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")