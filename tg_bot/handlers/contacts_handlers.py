from aiogram.types import Message

from tg_bot.common.db_commands import check_access
from tg_bot.loader import dp


@dp.message_handler(text='Связаться с нами')
async def contacts(message: Message):
    text = 'Связаться с администрацией сообщества вы можете написав нам:\n\n' \
           '<b>Telegram:</b> @sbalasanyan\n' \
           '<b>E-mail:</b> <a href="mailto:serg.balasanyan@gmail.com">serg.balasanyan@gmail.com</a>\n' \
           '<b>Web:</b> <a href="https://eto-business.ru">https://eto-business.ru</a>\n\n' \
           '<b>Наш информационный канал:</b> @eto_business'
    await message.delete()

    if not await check_access(message.from_user.username):
        text = '<b>У Вас нет доступа.</b>\n\n' + text

    await message.answer(text=text, disable_web_page_preview=True)
