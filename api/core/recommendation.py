import pandas as pd


def recommend(name: str, top=5):
    """
    Рекомендует 'top' похожих исполнителей на исполнителя 'name' пользователю
    :param name: запрос исполнителя от пользователя
    :param top: количество рекомендуемых исполнителей
    :return: рекомендованные исполнители
    """
    return ", ".join(pd.read_csv("api/data/TF_IDF.csv", index_col=0)[name].sort_values(ascending=False).index[1:top+1])
