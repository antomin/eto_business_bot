from aiogram.utils import executor
from django.core.management.base import BaseCommand

from tg_bot.handlers import dp


async def on_startup(dp):
    pass


class Command(BaseCommand):
    def handle(self, *args, **options):
        executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
