import os

from dotenv import load_dotenv
from joblib import Parallel, delayed

load_dotenv()
API_TOKEN = os.getenv('TOKEN')

names = ['Gorillaz',
         'Muse', 'Metallica',
         'Flo rida', 'grandson',
         'Oomph!', 'Imagine dragons',
         'Michael jackson',
         'Placebo',
         'Blues saraceno',
         'System of a down',
         'Arctic monkeys',
         'Lmfao', 'Starset',
         'Oh wonder', 'Coldplay',
         'The prodigy', 'Disturbed',
         'The neighbourhood', 'Tardigrade inferno',
         'Scorpions', 'Shinoda', 'Fall out boy',
         'Dope', 'Keane', 'Linkin park',
         'Papa roach', 'The cranberries',
         'Neffex', 'Thirty seconds to mars',
         'Drake', 'Billie eilish', 'Queen', 'Ac dc',
         "Guns n roses", 'Eminem', 'Thousand foot krutch',
         'Meg myers', 'Led zeppelin', 'Skindred', 'Rammstein',
         'The pretty reckless', 'Nickelback', 'Bring me the horizon',
         'Halsey', 'Black eyed peas', 'Maroon 5', 'Hollywood undead', 'Nazareth']


def get_lyrics(name: str, k: int):
    """
    Функция записывает определенное количество текстов песен 'k' в новый файл с именем исполнителя 'name'
    :param name: имя исполнителя
    :param k: кол-во песен для записи в файл
    :return:
    """
    import lyricsgenius as lg
    try:
        genius = lg.Genius(API_TOKEN, skip_non_songs=True,
                           excluded_terms=["(Remix)", "(Live)"],
                           remove_section_headers=True,
                           sleep_time=1,
                           retries=2,
                           verbose=True)
        songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
        s = [song.lyrics for song in songs]
        with open(f"../api/data/{name}.txt", "w") as f:
            f.write("\n \n".join(s))
        print(f"For {name} songs grabbed: {len(s)}")
    except:
        print(f"Some exception for {name}")


songs = Parallel(n_jobs=10, verbose=100)(delayed(get_lyrics)(i, 10) for i in names)
