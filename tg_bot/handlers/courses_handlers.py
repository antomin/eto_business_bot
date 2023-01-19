from aiogram.types import CallbackQuery, InputFile, Message
from asgiref.sync import sync_to_async
from django.conf import settings
from django.core.paginator import Paginator

from tg_bot.common.db_commands import get_courses
from tg_bot.keyboards.courses_keyboards import (course_kb, courses_category_kb,
                                                courses_cd)
from tg_bot.loader import dp


@dp.message_handler(text="Курсы")
async def courses(message: Message):
    await message.delete()
    await courses_list_categories(message)


async def courses_list_categories(message: Message | CallbackQuery, **kwargs):
    markup = await courses_category_kb()

    if isinstance(message, Message):
        await message.answer('Выберите категорию:', reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        if message.message.photo:
            await message.message.answer('Выберите категорию:', reply_markup=markup)
        else:
            await message.message.edit_text('Выберите категорию:', reply_markup=markup)

        await message.answer()


async def courses_list(callback: CallbackQuery, category_id, cur_page, **kwargs):
    cnt = 1

    courses = await get_courses(category_id)
    paginator = Paginator(courses, settings.ITEMS_IN_PAGE)
    page = await sync_to_async(paginator.page)(cur_page)
    page_list = page.object_list

    async for course in page_list:
        is_last = cnt == len(page_list)
        markup = await course_kb(course, category_id, cur_page, has_next_page=page.has_next(),
                                 has_prev_page=page.has_previous(), is_last=is_last)

        await callback.message.answer_photo(
            InputFile(f'{settings.MEDIA_ROOT}/{course.image_url}'),
            caption=f'<b>{course.title}</b>\n\n{course.description}',
            reply_markup=markup
        )

    cnt += 1
    await callback.answer()


@dp.callback_query_handler(courses_cd.filter())
async def navigate_courses(callback: CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category_id = callback_data.get('category_id')
    cur_page = callback_data.get('page')

    levels = {
        '0': courses_list_categories,
        '1': courses_list
    }

    await levels[current_level](
        callback,
        category_id=category_id,
        cur_page=cur_page
    )
