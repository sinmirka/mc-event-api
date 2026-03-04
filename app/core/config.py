import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set")

if not DISCORD_WEBHOOK:
    raise ValueError("DISCORD_WEBHOOK is not set")