from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_main = ReplyKeyboardMarkup(resize_keyboard=True, )
kb_main.row(
    KeyboardButton('TOП'),
    KeyboardButton('Категории'),
)
kb_main.row(
    KeyboardButton('Курсы'),
)
