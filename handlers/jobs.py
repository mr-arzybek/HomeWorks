from aiogram import types
import const


kb = types.ReplyKeyboardMarkup()
kb.add(types.KeyboardButton("Курьер"))
kb.add(types.KeyboardButton("Сборщик"))
kb.add(types.KeyboardButton("товаровед"))

async def show_jobs(call: types.CallbackQuery):
    await call.message.answer(
        text="Мы можем вам подобрать работу",
        reply_markup=kb
    )
    
async def show_courier(message: types.Message):
    await message.reply(const.COURIER)
    
async def show_collector(message: types.Message):
    await message.reply(const.COLLECTOR)
    
async def show_merchandiser(message: types.Message):
    await message.reply(const.MERCHANDISER)
