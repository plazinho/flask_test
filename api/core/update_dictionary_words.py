import os

from api.core.cleaner import clean_and_lemmatize


def update_dictionary_words(lyrics):
    songs_artists = dict()
    for artist in os.listdir('../../api/data/raw_data'):
        try:
            with open(f"../../api/data/raw_data/{artist}", encoding='utf-8', newline='') as f:
                lyrics = f.read()
                songs_artists[artist[:-4]] = clean_and_lemmatize(lyrics)
        except:
            print(f"Some exception for '{artist}'")