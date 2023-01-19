from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from tg_bot.common.db_commands import get_course_categories

courses_cd = CallbackData('courses_menu', 'level', 'category_id', 'page')


def make_callback_data(level, category_id='0', page='1'):
    return courses_cd.new(level=level, category_id=category_id, page=page)


async def courses_category_kb():
    cur_level = 0
    markup = InlineKeyboardMarkup(row_width=1)
    categories = await get_course_categories()

    async for category in categories:
        callback_data = make_callback_data(level=cur_level+1, category_id=category.id)
        markup.insert(InlineKeyboardButton(category.title, callback_data=callback_data))

    return markup


async def course_kb(course, category_id, cur_page, has_next_page=False, has_prev_page=False, is_last=False):
    cur_level = 1
    cur_page = int(cur_page)
    markup = InlineKeyboardMarkup()
    markup.insert(InlineKeyboardButton('Перейти', url=course.url))

    if is_last:
        pagination_btn = []

        if has_prev_page:
            pagination_btn.append(InlineKeyboardButton(
                text='<< Пред.',
                callback_data=make_callback_data(level=cur_level, category_id=category_id, page=str(cur_page-1))
            ))

        if has_next_page:
            pagination_btn.append(InlineKeyboardButton(
                text='След. >>',
                callback_data=make_callback_data(level=cur_level, category_id=category_id, page=str(cur_page+1))
            ))

        markup.row(*pagination_btn)

        markup.row(InlineKeyboardButton(
            text='Назад',
            callback_data=make_callback_data(level=cur_level-1, category_id=category_id)
        ))

        return markup



