import lyricsgenius as lg

from api.loader import API_TOKEN


def init_parser(name: str, k=20):
    """
    Функция записывает определенное количество текстов песен 'k' в файл с именем исполнителя 'name'
    Также в этой функции проверяется написание имени исполнителей 'name'
    из нашего изначального списка исполнителей init_names.txt
    с правильным написанием имени исполнителя 'true_name' в базе 'Genius', поэтому название файла записывается по 'true_name'
    :param name: имя исполнителя
    :param k: кол-во песен для записи
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
        songs, true_name = response.songs, response.name.replace('/', '_').replace('\u200b', '')  # записываем песни в songs и
                                                                                                  # берем правильное написание имени исп. в true_name
        s = [song.lyrics for song in songs]
        with open(f"api/data/raw_data/{true_name}.txt", "w", encoding="utf-8") as f:
            f.write("\n \n".join(s))
        print(f"For '{true_name}' songs grabbed: {len(s)}")
    except:
        print(f"Couldn't download '{name}'")
