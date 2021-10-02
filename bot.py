import logging
import time

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Инициализация локальной базы
import api.checkers.file_checker
#

from api.loader import TELEGRAM_TOKEN
from api.core.recommendation import recommend

from static.texts import INFO, START, INPUT_ERROR, HELP
from static.artist_list import artist_list
from static.artist_count import artist_count

# Логирование
logging.basicConfig(filename='log.log',
                    level=logging.INFO)

# Инициализация бота
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    logging.info(f'{user_name} запустил бота в {time.asctime()}, его id = {user_id}')
    await message.reply(START % user_name, parse_mode='Markdown')


@dp.message_handler(commands=['info'])
async def process_info_command(message: types.Message):
    await message.reply(INFO)


@dp.message_handler(commands=['help'])
async def process_info_command(message: types.Message):
    await message.reply(HELP)


@dp.message_handler(commands=['artists'])
async def process_artist_command(message: types.Message):
    await message.reply(artist_list())


@dp.message_handler(commands=['artists_count'])
async def process_artist_count_command(message: types.Message):
    await message.reply(artist_count())


@dp.message_handler()
async def echo_message(message: types.Message):
    txt = message.text
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    if message.content_type != 'text':
        await bot.send_message(user_id, INPUT_ERROR)
    elif len(txt) > 30:
        await bot.send_message(user_id, 'Пришли имя исполнителя длиной не более 30 символов')
    else:
        logging.info(f'Нам написал {user_name} в {time.asctime()}, его id = {user_id}')
        await bot.send_message(user_id, recommend(txt))


if __name__ == '__main__':
    executor.start_polling(dp)
