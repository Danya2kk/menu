import database
from aiogram import Dispatcher, types
from buttons import kb_main, kb_menu
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text


async def start(message: types.Message):
    await message.reply("Вас приветствует бот доставки еды", reply_markup=kb_main)


async def close(message: types.Message):
    await message.reply("Клавиатура закрыта, для открытия введите /start", reply_markup=ReplyKeyboardRemove())


async def help(message: types.Message):
    await message.reply('Тут будет helpa', reply_markup=kb_main)


async def menu(message: types.Message):
    meals = database.tables.selectMenu()
    await message.reply(str(meals), reply_markup=kb_menu)


async def back(message: types.Message):
    await message.reply('Вы возвращены в назад', reply_markup=kb_main)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(close, Text(equals='Закрыть', ignore_case=True))
    dp.register_message_handler(back, Text(equals='Назад', ignore_case=True))
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, Text(equals='Помощь', ignore_case=True))
    dp.register_message_handler(menu, Text(equals='Меню', ignore_case=True))
