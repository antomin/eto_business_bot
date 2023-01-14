from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           InputMediaPhoto)
from aiogram.utils.callback_data import CallbackData

from tg_bot.common.db_commands import (get_service, get_service_categories,
                                       get_service_subcategories, get_services)
from tg_bot.loader import bot

menu_cd = CallbackData('show_menu', 'level', 'category', 'subcategory', 'service')


def make_callback_data(level, category='_', subcategory='_', service='_'):
    return menu_cd.new(level=level, category=category, subcategory=subcategory, service=service)


async def categories_kb():
    cur_level = 0
    markup = InlineKeyboardMarkup(row_width=1)
    categories = await get_service_categories()

    async for category in categories:
        btn_text = category.title
        callback_data = make_callback_data(level=cur_level+1, category=category.id)
        markup.insert(InlineKeyboardButton(btn_text, callback_data=callback_data))

    return markup


async def subcategories_kb(category_id):
    cur_level = 1
    markup = InlineKeyboardMarkup(row_width=1)
    sub_categories = await get_service_subcategories(category_id)

    async for sub_category in sub_categories:
        btn_text = sub_category.title
        callback_data = make_callback_data(level=cur_level+1, category=category_id, subcategory=sub_category.id)
        markup.insert(InlineKeyboardButton(btn_text, callback_data=callback_data))

    markup.row(InlineKeyboardButton(text='Назад', callback_data=make_callback_data(level=cur_level-1)))

    return markup


async def services_kb(category_id, subcategory_id):
    cur_level = 2
    markup = InlineKeyboardMarkup(row_width=2)
    services = await get_services(subcategory_id)

    async for service in services:
        markup.add(
            InlineKeyboardButton('Email', url=service.email),
            InlineKeyboardButton('Telegram', url=f't.me/{service.tg}')
        )

    markup.row(InlineKeyboardButton(
        text='Назад',
        callback_data=make_callback_data(level=cur_level-1, category=category_id)))

    return markup
