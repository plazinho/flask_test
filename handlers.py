import asyncio
import time
import logging

from aiogram import types

from bot import bot, dp, loop
from api.loader import ADMIN_ID
from static.texts import INFO, START, INPUT_ERROR, HELP
from static.artist_list import artist_list
from static.artist_count import artist_count


async def startup(dispatcher):
    logging.info(f'Бот запущен в {time.asctime()}')
    await bot.send_message(chat_id=ADMIN_ID, text='Бот запущен')


async def shutdown(dispatcher):
    logging.info(f'Бот закончил работу в {time.asctime()}')
    await bot.send_message(chat_id=ADMIN_ID, text='Бот закончил работу')


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
async def process_help_command(message: types.Message):
    await message.reply(HELP)


@dp.message_handler(commands=['artists'])
async def process_artist_command(message: types.Message):
    await message.reply(artist_list())


@dp.message_handler(commands=['artists_count'])
async def process_artist_count_command(message: types.Message):
    await message.reply(artist_count())


async def please_wait(dispatcher):
    logging.info(f'Начали обновление локальной базы в {time.asctime()}')
    await bot.send_message(chat_id=ADMIN_ID, text=f'В локальной базе отсутствует исполнитель'
                                                  f' обновляем базу, это может занять 1-2 минуты')


@dp.message_handler()
async def user_request(message: types.Message):
    from api.core.recommendation import recommend
    txt = message.text
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    if len(txt) > 30:
        await bot.send_message(user_id, 'Пришли имя исполнителя длиной не более 30 символов')
    else:
        logging.info(f'Нам написал {user_name} в {time.asctime()}, его id = {user_id}. Содержание запроса: {txt}')
        await message.reply(recommend(txt, message))


@dp.message_handler(content_types='any')
async def unknown_message(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(user_id, INPUT_ERROR)
