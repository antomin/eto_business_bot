from aiogram import Bot, Dispatcher
from environs import Env

env = Env()
env.read_env()

TG_TOKEN = env.str('TG_TOKEN')

DB_USER = env.str('DB_USER')
DB_PASSWORD = env.str('DB_PASSWORD')
DB_HOST = env.str('DB_HOST')
DB_PORT = env.int('DB_PORT')
DB_NAME = env.str('DB_NAME')


bot = Bot(token=TG_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot=bot)
