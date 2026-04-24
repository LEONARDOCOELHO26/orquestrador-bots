import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("API_URL")

def fetch():
    try:
        r = requests.get(URL, timeout=5)
        print("Status:", r.status_code)
        print("Título:", r.json().get("title"))
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    for _ in range(3):
        fetch()
        time.sleep(3)
