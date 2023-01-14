from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from service_app.models import ServiceCategory
from tg_bot.common.db_commands import (get_categories, get_services,
                                       get_sub_categories)

menu_cb = CallbackData('show_menu', 'level', 'category', 'subcategory', 'service')
contacts_service = CallbackData('show_contacts', 'service_id')


def make_callback_data(level, category='_', subcategory='_', service='_'):
    return menu_cb.new(level=level, category=category, subcategory=subcategory, service=service)


async def categories_kb():
    cur_level = 0
    markup = InlineKeyboardMarkup(row_width=1)
    categories = get_categories()

    async for category in categories:
        btn_text = category.title
        callback_data = make_callback_data(level=cur_level+1, category=category.id)
        markup.insert(InlineKeyboardButton(btn_text, callback_data=callback_data))

    return markup


async def sub_categories_kb(category_id):
    cur_level = 1
    markup = InlineKeyboardMarkup()
    sub_categories = await get_sub_categories(category_id)

    async for sub_category in sub_categories:
        btn_text = sub_category.title
        callback_data = make_callback_data(level=cur_level+1, category=category_id, subcategory=sub_category.id)
        markup.insert(InlineKeyboardButton(btn_text, callback_data=callback_data))

    markup.row(InlineKeyboardButton(text='Назад', callback_data=make_callback_data(level=cur_level-1)))

    return markup


async def services_kb(subcategory_id, category_id):
    cur_level = 2
    markup = InlineKeyboardMarkup()
    services = await get_services(subcategory_id)

    for service in services:
        markup.add(
            InlineKeyboardButton('Email', url=service.email),
            InlineKeyboardButton('Telegram', url=service.tg)
        )

    markup.row(InlineKeyboardButton(
        text='Назад',
        callback_data=make_callback_data(level=cur_level-1, category=category_id)))

    return markup
