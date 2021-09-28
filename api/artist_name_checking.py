import os

from dotenv import load_dotenv
import lyricsgenius as lg

load_dotenv()
API_TOKEN = os.getenv('TOKEN')


def name_checker(name: str) -> str:
    """
    :param name: имя исполнителя, заданное пользователем
    :return: исправленное имя исполнителя, хранящееся в базе Genius
    """
    try:
        genius = lg.Genius(API_TOKEN,
                           skip_non_songs=True,
                           remove_section_headers=True,
                           sleep_time=1,
                           retries=2,
                           verbose=True)
        response = (genius.search_artist(name, max_songs=1))
        true_name = response.name
        return true_name
    except:
        print(f"Some exception for {name}")


for artist in os.listdir('../api/data'):
    os.rename(f'../api/data/{artist}',
              f'../api/data/{name_checker(artist[:-4]).replace("/", "_")}.txt')

try:
    os.rename(f'../api/data/\u200bgrandson.txt',
              f'../api/data/Grandson.txt')
except:
    print("can't find artist named 'grandson'")
