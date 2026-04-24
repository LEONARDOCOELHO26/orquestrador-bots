import time
from datetime import datetime

LOG_FILE = "heartbeat.log"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

if __name__ == "__main__":
    log("Bot iniciado")
    while True:
        log("Estou vivo")
        time.sleep(5)
