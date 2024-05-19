from dotenv import load_dotenv
import os

load_dotenv()

L_CHAT = os.getenv('L_CHAT')
OP_CHAT = os.getenv('OP_CHAT')
TOKEN = os.getenv('TOKEN')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
