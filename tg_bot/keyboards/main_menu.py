from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.row(
    KeyboardButton('ТОП'),
    KeyboardButton('Услуги'),
).row(
    KeyboardButton('Курсы'),
    KeyboardButton('Контакты'),
)
