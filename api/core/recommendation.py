import pandas as pd
from api.checkers.artist_checker import artist_checker


def recommend(name: str, top=5):
    """
    Рекомендует 'top' похожих исполнителей на исполнителя 'name' пользователю
    :param name: запрос исполнителя от пользователя
    :param top: количество рекомендуемых исполнителей
    :return: рекомендованные исполнители
    """
    name = artist_checker(name)
    return ", ".join(pd.read_csv("api/data/TF_IDF.csv", index_col=0)[name].sort_values(ascending=False).index[1:top+1])
