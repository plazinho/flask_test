import lyricsgenius as lg

from api.loader import API_TOKEN


def single_artist_parser(name: str, k=10):
    """
    Функция записывает определенное количество текстов песен 'k' в файл с именем исполнителя 'name'
    Название файла записывается по имени исполнителя 'name'
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
        songs = response.songs
        s = [song.lyrics for song in songs]
        with open(f"api/data/raw_data/{name}.txt", "w", encoding="utf-8") as f:
            f.write("\n \n".join(s))
        print(f"For '{name}' songs grabbed: {len(s)}")
    except:
        print(f"Some exception for '{name}', please try again")
