from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

topservices_cd = CallbackData('topservices', 'page')


def make_callback_data(page='1'):
    return topservices_cd.new(page=page)


async def topservices_kb(service, cur_page, has_next_page=False, has_prev_page=False, is_last=False):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Telegram', url=f't.me/{service.tg}'))

    if is_last:
        pagination_btn = []

        if has_prev_page:
            pagination_btn.append(InlineKeyboardButton(
                text='<< Пред.',
                callback_data=make_callback_data(page=cur_page - 1)
            ))

        if has_next_page:
            pagination_btn.append(InlineKeyboardButton(
                text='След. >>',
                callback_data=make_callback_data(page=cur_page + 1)
            ))

        markup.row(*pagination_btn)

    return markup
