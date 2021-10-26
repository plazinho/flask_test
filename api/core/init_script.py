"""
Скрипт для первого запуска.
Создает первоначальную локальную базу с исполнителями и их текстами песен из заданного списка исполнителей init_names.txt
"""
import os

from joblib import Parallel, delayed

from api.core.init_parser import init_parser
from api.core.update_artist_names import update_artist_names
from api.core.update_dictionary_words import update_dictionary_words
from api.core.lyrics_loader import lyrics_loader
from api.core.cleaner import clean_and_lemmatize
from api.core.tf_idf import tf_idf


with open("api/data/init_names.txt", 'r', encoding="utf-8") as file:  # файл с именами исполнителей для создания первоначальной базы
    names = file.read().strip().split('\n')

Parallel(n_jobs=32, verbose=100)(delayed(init_parser)(i, 12) for i in names)  # скачиваем тексты песен в папку data/raw_data

# записываем в файл artist_names.txt имена исполнителей, тексты песен которых удалось скачать
for artist in os.listdir("api/data/raw_data"):
    update_artist_names(artist[:-4])  # обрезаем '.txt'

# Создаем словарь dictionary_words.json, состоящий из исполнителей(ключи) и всех их обработанных текстов песен(значения)
# На основе этого словаря производится расчет матрицы близости в функции tf_idf
with open('api/data/artist_names.txt', 'r', encoding="utf-8") as file:
    names = file.read().strip().split('\n')
    for artist in names:
        update_dictionary_words(artist, clean_and_lemmatize(lyrics_loader(artist)))

# Рассчитываем матрицу косинусной близости исполнителей и записываем ее в файл TF_IDF.csv
tf_idf()
