import asyncio

from api.checkers.name_checker import name_checker
from api.core.single_artist_parser import single_artist_parser
from api.core.update_artist_names import update_artist_names
from api.core.cleaner import clean_and_lemmatize
from api.core.lyrics_loader import lyrics_loader
from api.core.update_dictionary_words import update_dictionary_words
from api.core.tf_idf import tf_idf


def artist_checker(name: str, message) -> str:
    """
    Функция проверяет наличие исполнителя в локальной базе.
    Если его нет, то отправляется запрос в 'Genius' API на скачивание текстов песен
    с дальнейшим обновлением локальной базы данных
    :param name: Имя исполнителя
    :param message: входные данные от пользователя, чтобы иметь возможность ответить ему
    :return:
    """
    name = name_checker(name, message)
    with open("api/data/artist_names.txt", "r", encoding="utf-8") as file:
        names = file.read().strip().split('\n')
        if name in names:
            return name
        else:
            from handlers import dp, loop, please_wait
            loop.create_task(please_wait(dp))
            print(f"Couldn't find '{name}' in local database. Updating database, please wait...")

            single_artist_parser(name)

            update_artist_names(name)

            update_dictionary_words(name, clean_and_lemmatize(lyrics_loader(name)))

            tf_idf()

            return name
