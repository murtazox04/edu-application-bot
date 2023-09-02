from pathlib import Path

from aiogram import Bot, Dispatcher, Router, enums
from aiogram.fsm.storage.memory import MemoryStorage

from decouple import config


TOKEN = config('BOT_TOKEN')

BASE_DIR = Path(__file__).parent

bot = Bot(token=TOKEN, parse_mode=enums.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()
