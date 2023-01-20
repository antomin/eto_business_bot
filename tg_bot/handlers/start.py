from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from tg_bot.keyboards.main_menu import kb_main
from tg_bot.loader import dp


@dp.message_handler(CommandStart())
async def echo(message: Message):
    await message.answer(
        text=f'Здравствуйте, {message.from_user.first_name}!\n'
             f'Меня зовут Сергей, я ваш личный гид по сообществу «Бизнеси Ничего Личного».\n\n'
             f'Нажмите на интересующий вас раздел:',
        reply_markup=kb_main
    )
