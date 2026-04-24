import random
from datetime import datetime

acoes = ["investir", "economizar", "gastar", "não fazer nada"]

if __name__ == "__main__":
    print(f"{datetime.now()} - Decisão: {random.choice(acoes)}")
