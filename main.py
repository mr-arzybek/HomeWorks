from aiogram import executor
from aiogram.dispatcher.filters import Text
from config import dp
import logging
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
from handlers.user_info import (
    UserForm,
    start_user_dialog,
    process_age,
    process_name,
    process_address,
    process_day,
    mail,
    not_mail
)





if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_help, commands=['help'])
    dp.register_message_handler(cmd_myinfo, commands=['myinfo'])
    dp.register_message_handler(cmd_picture, commands=['picture'])
    
    dp.register_callback_query_handler(show_jobs, Text(equals="jobs"))
    dp.register_message_handler(show_courier, Text(startswith="Курьер"))
    dp.register_message_handler(show_collector, Text(startswith="Сборщик"))
    dp.register_message_handler(show_merchandiser, Text(startswith="товаровед"))
    
    dp.register_message_handler(start_user_dialog, commands=["form"])
    dp.register_message_handler(process_name, state=UserForm.name)
    dp.register_message_handler(process_age, state=UserForm.age)
    dp.register_message_handler(process_address, state=UserForm.address)
    dp.register_message_handler(process_day, state=UserForm.day)
    dp.register_callback_query_handler(mail, Text(startswith="да"))
    dp.register_callback_query_handler(not_mail, Text(startswith="нет"))
    executor.start_polling(dp, skip_updates=True)