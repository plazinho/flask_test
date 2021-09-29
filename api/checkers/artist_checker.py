import os

from api.checkers.name_checker import name_checker
from api.core.single_artist_parser import single_artist_parser
from api.core.update_artist_names import update_artist_names


def artist_checker(name: str) -> str:
    """
    Функция проверяет наличие исполнителя в локальной базе.
    Если его нет, то отправляется запрос в 'Genius' API на скачивание текстов песен
    с дальнейшим обновлением локальной базы данных
    :param name: имя исполнителя
    :return:
    """
    name = name_checker(name)
    with open("../../api/data/artist_names.txt", 'r', encoding='ISO-8859-1') as file:
        names = file.read().strip().split('\n')
        if name in names:
            return name
        else:
            print(f"Couldn't find '{name}' in local database. Updating database, please wait...")
            single_artist_parser(name)
            update_artist_names(name)
            return name


artist_checker('Celldweller')