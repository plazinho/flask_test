# import os

from joblib import Parallel, delayed
import lyricsgenius as lg

from api.loader import API_TOKEN

with open("../../api/data/init_names.txt", 'r') as file:
    names = file.read().split('\n')


def get_lyrics(name: str, k: int):
    """
    Функция записывает определенное количество текстов песен 'k' в новый файл с именем исполнителя 'name'
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
        songs, true_artist_name = response.songs, response.name
        s = [song.lyrics for song in songs]
        with open(f"../../api/data/raw_data/{true_artist_name}.txt", "w") as f:
            f.write("\n \n".join(s))
        print(f"For {true_artist_name} songs grabbed: {len(s)}")
    except:
        print(f"Some exception for {name}")


songs = Parallel(n_jobs=10, verbose=100)(delayed(get_lyrics)(i, 15) for i in names)
