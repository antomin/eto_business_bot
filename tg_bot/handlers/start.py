from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from tg_bot.keyboards.main_menu import kb_main
from tg_bot.loader import dp


@dp.message_handler(CommandStart())
async def echo(message: Message):
    await message.answer(f'Приветствую, {message.from_user.first_name}!!!', reply_markup=kb_main)
