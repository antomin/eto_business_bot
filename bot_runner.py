from aiogram.utils import executor

from tg_bot.handlers import dp

if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        pass
