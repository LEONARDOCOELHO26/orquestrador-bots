import random
from datetime import datetime

def gerar_usuario():
    saldo = random.randint(100, 5000)
    gasto = random.randint(50, 1000)
    score = max(0, min(1000, saldo - gasto))

    return {
        "saldo": saldo,
        "gasto": gasto,
        "score": score,
        "timestamp": str(datetime.now())
    }

if __name__ == "__main__":
    print("Simulação:", gerar_usuario())
