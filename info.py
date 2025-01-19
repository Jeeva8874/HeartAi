# ©️biisal jai shree krishna 😎
from os import environ
from dotenv import load_dotenv

load_dotenv()

API_ID = environ.get("API_ID" , "22977776")
API_HASH = environ.get("API_HASH" , "2ac7223d720bdeec757cbc88ced57224")
BOT_TOKEN = environ.get("BOT_TOKEN" , "7739144267:AAEES7LHsbIDqivIP2Huug4PY-08YaM27p4")
ADMIN = int(environ.get("ADMIN" , "6762558871"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1002162863916"))
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002391269521")
MONGO_URL = environ.get("MONGO_URL" , "mongodb://localhost:27017")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1002367524502")
)
FSUB = environ.get("FSUB", True)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", True
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
