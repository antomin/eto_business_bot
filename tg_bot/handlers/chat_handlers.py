from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from tg_bot.common.db_commands import check_access
from tg_bot.handlers.contacts_handlers import contacts
from tg_bot.loader import dp


@dp.message_handler(text='Чат сообщества')
async def chat(message: Message):
    await message.delete()

    if not await check_access(message.from_user.username):
        await contacts(message)
        return

    await message.answer(text='Перейти в наш', reply_markup=InlineKeyboardMarkup().row(
        InlineKeyboardButton('чат', url='t.me/+wKBGq59JCV41YzAy')
    ))
