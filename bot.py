import asyncio
import logging

from aiogram import Bot, Dispatcher, executor

# Инициализация локальной базы
import api.checkers.file_checker
#

from api.loader import TELEGRAM_TOKEN

# Логирование
logging.basicConfig(filename='log.log',
                    level=logging.INFO)

# Инициализация бота
loop = asyncio.get_event_loop()
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers import startup, shutdown, dp
    executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown)
