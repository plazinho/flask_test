import os
from dotenv import load_dotenv
import lyricsgenius as lg

load_dotenv()
API_TOKEN = os.getenv('TOKEN')


def name_checker(name):
    # if name not in names:
    try:
        genius = lg.Genius(API_TOKEN, skip_non_songs=True, remove_section_headers=True)
        response = (genius.search_artist(name, max_songs=1, sort='popularity'))
        true_name = response.name
        return true_name
    except:
        print(f"some exception at {name}")
    # return name


for i in os.listdir('C:/Users/apofi/flask_test/api/data'):
    os.rename(f'C:/Users/apofi/flask_test/api/data/{i}',
              f'C:/Users/apofi/flask_test/api/data/{name_checker(i[:-4])}.txt')
