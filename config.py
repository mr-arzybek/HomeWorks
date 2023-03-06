from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))

# bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

scheduler = AsyncIOScheduler()


# BOT_TOKEN_ADMIN = 'AAHjbU_-H9C9i4S5iUd-wtqUIwjVKDe-HEI'
# bot2 = Bot(token=BOT_TOKEN_ADMIN)
# dp2 = Dispatcher(bot2, storage=storage)