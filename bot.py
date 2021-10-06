import logging

from aiogram import Bot, Dispatcher, executor

from api.loader import TELEGRAM_TOKEN

# Логирование
logging.basicConfig(filename='log.log',
                    level=logging.INFO)

# Инициализация бота
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


if __name__ == '__main__':
    from handlers import startup, shutdown, dp
    executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown)
