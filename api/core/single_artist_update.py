from api.core.single_artist_parser import single_artist_parser
from api.core.update_artist_names import update_artist_names
from api.core.cleaner import clean_and_lemmatize
from api.core.lyrics_loader import lyrics_loader
from api.core.update_dictionary_words import update_dictionary_words
from api.core.tf_idf import tf_idf


def single_artist_update(name: str) -> str:
    """
    Функция обновляет локальную базу новым исполнителем
    :param name: имя исполнителя
    :return: имя исполнителя
    """

    print(f"Couldn't find '{name}' in local database. Updating database, please wait...")

    # 1. Обращается к базе 'Genius' и скачивает тексты песен исполнителя
    single_artist_parser(name)

    # 2. Обновляет файл с именами исполнителей, хранящихся в локальной базе
    update_artist_names(name)

    # 3. Обновляет словарь, состоящий из исполнителей(ключи) и всех их обработанных текстов песен(значения)
    update_dictionary_words(name, clean_and_lemmatize(lyrics_loader(name)))

    # 4. Производит расчет матрицы косинусной близости текстов песен с помощью показателя TF_IDF
    tf_idf()

    return name
