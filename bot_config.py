import configparser
import os
from dotenv import load_dotenv

load_dotenv()

config = configparser.ConfigParser()
config.read("config.ini")

modo = config.get("geral", "modo", fallback="default")
api_key = os.getenv("API_KEY", "sem-chave")

print("Modo:", modo)
print("API KEY:", api_key)
