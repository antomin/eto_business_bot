from aiogram.types import CallbackQuery, InputFile, Message
from asgiref.sync import sync_to_async
from django.conf import settings
from django.core.paginator import Paginator

from tg_bot.common.db_commands import check_access, get_topservices
from tg_bot.common.misc import generate_service_desc
from tg_bot.handlers.contacts_handlers import contacts
from tg_bot.keyboards.topservices_keyboards import (topservices_cd,
                                                    topservices_kb)
from tg_bot.loader import dp


@dp.message_handler(text='Новые Резиденты')
async def top_services(message: Message):
    if not await check_access(message.from_user.username):
        await contacts(message)
        return
    await message.delete()
    await get_top_list(message)


async def get_top_list(message: Message | CallbackQuery, cur_page=1):
    cnt = 1

    services = await get_topservices()
    paginator = Paginator(services, settings.ITEMS_FOR_PAGE)
    page = await sync_to_async(paginator.page)(cur_page)
    page_list = page.object_list

    async for service in page_list:
        is_last = cnt == len(page_list)

        text = await generate_service_desc(service)

        markup = await topservices_kb(service, page.number, has_next_page=page.has_next(),
                                      has_prev_page=page.has_previous(), is_last=is_last)
        if isinstance(message, Message):
            await message.answer_photo(
                InputFile(f'{settings.MEDIA_ROOT}/{service.image_url}'), caption=text, reply_markup=markup
            )

        elif isinstance(message, CallbackQuery):
            await message.message.answer_photo(
                InputFile(f'{settings.MEDIA_ROOT}/{service.image_url}'),
                caption=f'<b>{service.first_name} {service.last_name}</b>\n\n{service.description}\n\n',
                reply_markup=markup
            )
            await message.answer()

        cnt += 1


@dp.callback_query_handler(topservices_cd.filter())
async def navigate_topservices(callback: CallbackQuery, callback_data: dict):
    page = callback_data.get('page')

    await get_top_list(callback, cur_page=page)
