from aiogram.types import CallbackQuery, InputFile, Message
from asgiref.sync import sync_to_async
from django.conf import settings
from django.core.paginator import Paginator

from tg_bot.common.db_commands import check_access, get_services
from tg_bot.handlers.contacts_handlers import contacts
from tg_bot.keyboards.services_keyboards import (categories_kb, service_kb,
                                                 services_cd, subcategories_kb)
from tg_bot.loader import dp


@dp.message_handler(text='Наши Резиденты')
async def categories(message: Message):
    if not await check_access(message.from_user.username):
        await contacts(message)
        return
    await message.delete()
    await list_categories(message)


async def list_categories(message: Message | CallbackQuery, **kwargs):
    markup = await categories_kb()

    if isinstance(message, Message):
        await message.answer('Выберите категорию:', reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        await message.message.edit_text('Выберите категорию:', reply_markup=markup)


async def list_subcategories(callback: CallbackQuery, category_id, **kwargs):
    markup = await subcategories_kb(category_id)

    if callback.message.photo:
        await callback.message.answer('Выберите подкатегорию:', reply_markup=markup)
    else:
        await callback.message.edit_text('Выберите подкатегорию:', reply_markup=markup)

    await callback.answer()


async def list_services(callback: CallbackQuery, category_id, subcategory_id, page, **kwargs):
    cnt = 1

    services = await get_services(subcategory_id)
    paginator = Paginator(services, settings.ITEMS_FOR_PAGE)
    page = await sync_to_async(paginator.page)(page)
    page_list = page.object_list

    async for service in page_list:
        is_last = cnt == len(page_list)

        text = f'<b>{service.first_name} {service.last_name}</b>\n\n' \
               f'<b>Обо мне:</b>\n{service.description}'

        if service.email:
            text += f'\n\n<b>Email:</b> <code>{service.email}</code>'

        if service.phone:
            text += f'\n\n<b>Тел.:</b> {service.phone}'

        if service.web_url:
            text += f'\n\n<b>Сайт:</b> <a href="{service.web_url}">{service.web_url}</a>'

        markup = await service_kb(service, category_id, subcategory_id, is_last=is_last, cur_page=page.number,
                                  has_next_page=page.has_next(), has_prev_page=page.has_previous())

        await callback.message.answer_photo(
            InputFile(f'{settings.MEDIA_ROOT}/{service.image_url}'), caption=text, reply_markup=markup
        )

        cnt += 1

    await callback.answer()


@dp.callback_query_handler(services_cd.filter())
async def navigate_services(callback: CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category_id = callback_data.get('category_id')
    subcategory_id = callback_data.get('subcategory_id')
    page = callback_data.get('page')

    levels = {
        '0': list_categories,
        '1': list_subcategories,
        '2': list_services
    }

    await levels[current_level](
        callback,
        category_id=category_id,
        subcategory_id=subcategory_id,
        page=page
    )
