# import os

from joblib import Parallel, delayed
import lyricsgenius as lg

from api.loader import API_TOKEN

with open("../../api/data/init_names.txt", 'r', encoding='ISO-8859-1') as file:  # файл с именами исполнителей для создания
    names = file.read().strip().split('\n')                                              # первоначальной базы

missed = []                                                                      # исполнители, которых не удалось записать


def init_parser(name: str, k=15):
    """
    Функция записывает определенное количество текстов песен 'k' в файл с именем исполнителя 'name'
    Название файла записывается по имени исполнителя 'true_name' из базы 'Genius'
    :param name: имя исполнителя
    :param k: кол-во песен для записи в файл
    :return:
    """
    try:
        genius = lg.Genius(API_TOKEN, skip_non_songs=True,
                           excluded_terms=["(Remix)", "(Live)"],
                           remove_section_headers=True,
                           sleep_time=1,
                           retries=2,
                           verbose=True)
        response = genius.search_artist(name, max_songs=k, sort='popularity')
        songs, true_name = response.songs, response.name.replace('/', '_').replace('\u200b', '')
        s = [song.lyrics for song in songs]
        with open(f"../../api/data/raw_data/{true_name}.txt", "w") as f:
            f.write("\n \n".join(s))
        print(f"For '{true_name}' songs grabbed: {len(s)}")
    except:
        missed.append(name)


if len(missed) > 0:
    print(f"Some exceptions for {missed}")

songs = Parallel(n_jobs=32, verbose=100)(delayed(init_parser)(i, 15) for i in names)
