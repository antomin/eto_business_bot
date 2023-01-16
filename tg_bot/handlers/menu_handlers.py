from webbrowser import open as browser_open

from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, InputFile, Message
from django.conf import settings

from tg_bot.common.db_commands import get_services
from tg_bot.keyboards.services_keyboards import (categories_kb, menu_cd,
                                                 service_kb, subcategories_kb)
from tg_bot.loader import dp


@dp.message_handler(Command('Категории'))
async def categories(message: Message):
    await list_categories(message)


@dp.callback_query_handler(lambda callback: callback.data and callback.data.startswith('mailto__'))
async def open_mail(callback: CallbackQuery):
    email = callback.data.split('__')[-1]
    browser_open(f'mailto:{email}')
    await callback.answer()


async def list_categories(message: Message | CallbackQuery, **kwargs):
    markup = await categories_kb()

    if isinstance(message, Message):
        await message.answer('Выберите категорию', reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        await message.message.edit_text('Выберите категорию:', reply_markup=markup)


async def list_subcategories(callback: CallbackQuery, category_id, **kwargs):
    markup = await subcategories_kb(category_id)
    if callback.message.photo:
        await callback.message.answer('Выберите подкатегорию:', reply_markup=markup)
    else:
        await callback.message.edit_text('Выберите подкатегорию:', reply_markup=markup)


async def list_services(callback: CallbackQuery, category_id, subcategory_id, **kwargs):
    cnt = 1
    services = await get_services(subcategory_id)
    async for service in services:
        markup = await service_kb(service, category_id, is_last=True if cnt == len(services) else False)
        await callback.message.answer_photo(
            InputFile(f'{settings.MEDIA_ROOT}/{service.image_url}'),
            caption=f'<b>{service.first_name} {service.last_name}</b>\n\n{service.description}',
            reply_markup=markup
        )
        cnt += 1


@dp.callback_query_handler(menu_cd.filter())
async def navigate(callback: CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category_id = callback_data.get('category')
    subcategory_id = callback_data.get('subcategory')
    service_id = callback_data.get('service')

    levels = {
        '0': list_categories,
        '1': list_subcategories,
        '2': list_services
    }

    await levels[current_level](
        callback,
        category_id=category_id,
        subcategory_id=subcategory_id,
        service_id=service_id
    )
