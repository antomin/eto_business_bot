from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message

from tg_bot.keyboards.menu_keyboards import categories_kb
from tg_bot.loader import dp


@dp.message_handler(Command('Категории'))
async def categories(message: Message):
    await list_categories(message)


async def list_categories(message: Message | CallbackQuery):
    markup = await categories_kb()

    if isinstance(message, Message):
        await message.answer('Выберите категорию', reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        await message.message.edit_reply_markup(markup)
