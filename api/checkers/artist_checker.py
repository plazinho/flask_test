# import lyricsgenius as lg
# from api.loader import API_TOKEN
# def input_checker(name):
#     try:
#         genius = lg.Genius(API_TOKEN,skip_non_songs=True, remove_section_headers=True)
#         response = (genius.search_artist(name, max_songs=1, sort='popularity'))
#         true_name = response.name
#         return true_name
#     except:
#         return name
import os
from api.checkers.name_checker import name_checker
# name = name_checker()
def artist_checker(artist_name):
    name = name_checker(artist_name)
    if name in os.listdir('api/database/artist_names.txt'):
        return artist_name
    else:
        return artist_name

