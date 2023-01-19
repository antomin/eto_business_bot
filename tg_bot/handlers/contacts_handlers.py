from aiogram.types import Message

from tg_bot.loader import dp


@dp.message_handler(text='Контакты')
async def contacts(message: Message):
    await message.delete()
    await message.answer('Контакты')
