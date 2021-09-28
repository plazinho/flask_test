import os

from dotenv import load_dotenv
from joblib import Parallel, delayed

load_dotenv()
API_TOKEN = os.getenv('TOKEN')

names = ['Gorillaz',
         'Muse', 'Metallica',
         'Flo rida', 'Grandson',
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
         'Drake', 'Billie eilish', 'Queen', 'Ac/dc',
         "Guns'n'roses", 'Eminem', 'Thousand foot krutch',
         'Meg myers', 'Led zeppelin', 'Skindred', 'Rammstein',
         'The pretty reckless', 'Nickelback', 'Bring me the horizon',
         'Halsey', 'Black eyed peas', 'Maroon 5', 'Hollywood undead', 'Nazareth']


def get_lyrics(name, k):
    c = 0
    import lyricsgenius as lg
    try:
        genius = lg.Genius(API_TOKEN, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                           remove_section_headers=True)
        songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
        s = [song.lyrics for song in songs]
        with open(f"api/data/{name}.txt", "w") as f:
            f.write("\n \n".join(s))
        c += 1
        print(f"Songs grabbed:{len(s)}")
    except:
        print(f"some exception at {name}: {c}")


songs = Parallel(n_jobs=30, verbose=1)(delayed(get_lyrics)(i, 10) for i in names)
