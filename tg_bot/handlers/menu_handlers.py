from typing import Union

from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message

from tg_bot.keyboards.menu_keyboards import categories_kb
from tg_bot.loader import dp


@dp.message_handler(Command('Категории'))
async def categories(message: Message):
    await list_categories(message)


async def list_categories(message: Union[Message, CallbackQuery], **kwargs):
    markup = await categories_kb()
