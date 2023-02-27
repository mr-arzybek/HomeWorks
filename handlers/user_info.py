from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery


class UserForm(StatesGroup):
    name = State()
    age = State()
    address = State()
    day = State()


async def start_user_dialog(message: types.Message):
    await UserForm.name.set()
    await message.answer("Как вас зовут?")
    await message.delete()


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # сохраяем данные о имени
        data['name'] = message.text
    
    await UserForm.next()
    await message.answer("Сколько вам лет?")


async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isnumeric():
        await message.reply("Вводите только цифры")
        await message.answer("Сколько вам лет?")
    else:
        async with state.proxy() as data:
            # сохраняем данные о возрасте
            data['age'] = age
        await UserForm.next()
        await message.answer("Какой у вас адрес?")


async def process_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # сохраяем данные о адресе
        data['address'] = message.text
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
        kb.add(*buttons)

    await UserForm.next()
    await message.answer("В какой день недели вам удобно получить товар?\n"
                         "Мы работаем пн-сб, воскресенье выходной", reply_markup=kb)


async def process_day(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # сохраяем данные о дне недели для получения товара
        data['day'] = message.text
        buttons = [
            types.InlineKeyboardButton(text='да', callback_data='да'),
            types.InlineKeyboardButton(text='нет', callback_data='нет'),
            types.InlineKeyboardButton(text='готово', callback_data='нет')
        ]
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb.add(*buttons)
        print(data)

    await state.finish()
    await message.answer(
        f"""
        Спасибо за то что пользуетесь нашим сервисом, вы хотите оставить сообщение?
        нвжмите готово после того как напишите отзыв 
        или 
        нет для завершения опроса!
        """,
        reply_markup=kb
                         )


async def mail(callback: CallbackQuery):
    """
    обработчик, чтоб принять сообщение
    """
    await callback.answer()
    message = callback.message
    await message.bot.send_message(
        text=f'{callback.from_user.first_name} мы передадим твое сообщение админам!',
        chat_id=message.chat.id
    )


async def not_mail(callback: CallbackQuery):
    """
    обработчик, чтоб попращаться
    """
    await callback.answer()
    message = callback.message
    await message.bot.send_message(
        text=f'{callback.from_user.first_name} до свидания!',
        chat_id=message.chat.id
    )