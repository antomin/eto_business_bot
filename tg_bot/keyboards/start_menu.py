from aiogram.dispatcher.filters import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.row(
    KeyboardButton('/Категории'),
)
