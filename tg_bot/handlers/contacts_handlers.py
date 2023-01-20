from aiogram.types import Message

from tg_bot.loader import dp


@dp.message_handler(text='Связаться с нами')
async def contacts(message: Message):
    await message.delete()
    await message.answer('Связаться с администрацией сообщества вы можете написав нам:\n\n'
                         '<b>Telegram:</b> @sbalasanyan\n'
                         '<b>E-mail:</b> <a href="mailto:serg.balasanyan@gmail.com">serg.balasanyan@gmail.com</a>\n'
                         '<b>Web:</b> <a href="https://eto-business.ru">https://eto-business.ru</a>\n\n'
                         '<b>Наш информационный канал:</b> @eto_business',
                         disable_web_page_preview=True)
