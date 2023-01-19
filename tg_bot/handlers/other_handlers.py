from aiogram.types import Message

from tg_bot.loader import dp


@dp.message_handler()
async def other(message: Message):
    await message.delete()
