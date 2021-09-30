from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import json


def tf_idf():
    """
    Функция производит расчет матрицы косинусной близости текстов песен с помощью показателя TF_IDF
    На основе этой матрицы и будет осуществляться рекомандация исполнителей пользователю
    :return:
    """
    with open("api/data/dictionary_words.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    tfidf = TfidfVectorizer(ngram_range=(1, 4))
    tfidf_representation = tfidf.fit_transform(data.values())

    artists_similarity = cosine_similarity(tfidf_representation)

    pd.DataFrame(artists_similarity, index=data.keys(), columns=data.keys()).to_csv("api/data/TF_IDF.csv")
