from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

EMAILS_FILEPATH = Path(os.getenv("EMAILS_FILEPATH"))
TELEGRAM_TEXT_FILEPATH = Path(os.getenv("TELEGRAM_TEXT_FILEPATH"))
BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")