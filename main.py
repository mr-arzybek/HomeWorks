from aiogram import executor
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
from os import getenv
from config import dp
from handlers.admin import (
    check_bad_words,
    ban_user,
    ban_user_warning
)
import logging
logging.basicConfig(level=logging.INFO)
load_dotenv()

if __name__ == "__main__":
    dp.register_message_handler(check_bad_words)
    dp.register_callback_query_handler(ban_user_warning, Text(startswith="abuser_name_warning"))
    dp.register_callback_query_handler(ban_user, Text(startswith="abuser_id"))
    print('hello')
    executor.start_polling(dp, skip_updates=True)