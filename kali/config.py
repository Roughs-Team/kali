# загружаем из .env

from dotenv import load_dotenv
import os

load_dotenv()

VK_GROUP_TOKEN = os.getenv("VK_GROUP_TOKEN")
VK_GROUP_ID = int(os.getenv("VK_GROUP_ID"))

BOT_NAME = os.getenv("BOT_NAME")