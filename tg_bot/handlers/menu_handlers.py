from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message

from tg_bot.keyboards.services_keyboards import (categories_kb, menu_cd,
                                                 services_kb, subcategories_kb)
from tg_bot.loader import dp


@dp.message_handler(Command('Категории'))
async def categories(message: Message):
    await list_categories(message)


async def list_categories(message: Message | CallbackQuery, **kwargs):
    markup = await categories_kb()

    if isinstance(message, Message):
        await message.answer('Выберите категорию', reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        await message.message.edit_text('Выберите категорию:', reply_markup=markup)


async def list_subcategories(callback: CallbackQuery, category_id, **kwargs):
    markup = await subcategories_kb(category_id)
    await callback.message.edit_text('Выберите подкатегорию:', reply_markup=markup)


async def list_services(callback: CallbackQuery, subcategory_id, category_id, **kwargs):
    markup = await services_kb(subcategory_id=subcategory_id, category_id=category_id)
    await callback.message.edit_text('Список услуг:', reply_markup=markup)


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
