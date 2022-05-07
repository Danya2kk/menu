from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_menu = KeyboardButton('Меню')
button_help = KeyboardButton('Помощь')
button_order = KeyboardButton('Заказать')
button_close = KeyboardButton('Закрыть')

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(button_menu).insert(button_order).insert(button_help).add(button_close)

but_burgers = KeyboardButton('Бургеры')
but_pizza = KeyboardButton('Пицца')
but_roll = KeyboardButton('Роллы')
but_drinks = KeyboardButton('Напитки')
but_dessert = KeyboardButton('Десерты')
but_back = KeyboardButton('Назад')

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.add(but_burgers).insert(but_pizza).insert(but_roll).add(but_drinks).insert(but_dessert).add(but_back)
