from aiogram import types
import random

kb = types.InlineKeyboardMarkup()
kb.add(types.InlineKeyboardButton(
    text="Вакансии",
    callback_data="jobs"
))
kb.add(types.InlineKeyboardButton(
    text="О нас",
    callback_data="about"
))

async def cmd_start(message: types.Message):
    await message.answer(
    f"""
    Привет {message.from_user.full_name}
    Мы HR компания BAUMAN !                         
    """,
    reply_markup=kb
    )
    await message.delete()
    
async def cmd_help(message: types.Message):
    await message.answer("""
        /start - приветствует по имени
        /help - показывает список команд
        /myinfo - отправляет пользователю его данные(id, first_name, username)
        /picture - отправляет слуайную картинку
                         """)
    await message.delete()
    
async def cmd_myinfo(message: types.Message):
    await message.answer(f"""
        id: {message.from_user.id}
        First_name: {message.from_user.first_name}
        User_name: {message.from_user.username}
                         """)
    await message.delete()
    
async def cmd_picture(message: types.Message):
    img = ["img/img_1.png", "img/img_2.png", "img/img_3.png", "img/img_4.png"]
    photo = open(random.choice(img), 'rb')
    await message.answer_photo(
        photo
    )
    await message.delete()