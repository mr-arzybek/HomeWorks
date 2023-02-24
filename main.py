from aiogram import executor
from config import dp
from aiogram.dispatcher.filters import Text
from handlers.basic import (
    cmd_start,
    cmd_help,
    cmd_myinfo,
    cmd_picture
)
from handlers.jobs import (
    show_courier,
    show_collector,
    show_jobs,
    show_merchandiser
)


if __name__ == "__main__":
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_help, commands=['help'])
    dp.register_message_handler(cmd_myinfo, commands=['myinfo'])
    dp.register_message_handler(cmd_picture, commands=['picture'])
    
    dp.register_callback_query_handler(show_jobs, Text(equals="jobs"))
    dp.register_message_handler(show_courier, Text(startswith="Курьер"))
    dp.register_message_handler(show_collector, Text(startswith="Сборщик"))
    dp.register_message_handler(show_merchandiser, Text(startswith="товаровед"))
    print("hello")
    executor.start_polling(dp)