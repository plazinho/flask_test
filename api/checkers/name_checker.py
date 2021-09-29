# import os

import lyricsgenius as lg

from api.loader import API_TOKEN
from api.checkers.input_checker import input_checker


def name_checker(name: str) -> str:
    """
    Функция исправляет имя исполнителя из запроса пользователя по имени исполнителя из базы 'Genius'
    :param name: имя исполнителя от пользователя
    :return: исправленное имя исполнителя, хранящееся в базе Genius
    """
    name = input_checker(name)
    try:
        genius = lg.Genius(API_TOKEN,
                           skip_non_songs=True,
                           remove_section_headers=True,
                           sleep_time=1,
                           retries=2,
                           verbose=True)
        response = genius.search_artist(name, max_songs=1)
        true_name = response.name.replace('/', '_').replace('\u200b', '')
        return true_name
    except:
        print(f"Couldn't find '{name}' in database, check the spelling of the artist's name")




