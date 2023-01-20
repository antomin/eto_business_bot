from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.row(
    KeyboardButton('Новые Резиденты')
).row(
    KeyboardButton('Наши Резиденты'),
    KeyboardButton('Обучение и Курсы'),
).row(
    KeyboardButton('Чат сообщества'),
    KeyboardButton('Связаться с нами'),
)
