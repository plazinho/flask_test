import json


def update_dictionary_words(name, lyrics):
    """
    Функция обновляет словарь, состоящий из исполнителей(ключи) и всех их обработанных текстов песен(значения)
    На основе этого словаря производится расчет матрицы близости в функции tf_idf
    :param name: Новый исполнитель
    :param lyrics: Текст его песен
    :return:
    """
    with open("api/data/dictionary_words.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        data[name] = lyrics
    with open("api/data/dictionary_words.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=16)
