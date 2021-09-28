from api.artists_similarity_database import df


def recommend(artist_name: str, top=5) -> str:
    """
    Рекомендует 'top' похожих исполнителей на исполнителя 'artist_name' пользователю
    :param artist_name:
    :param top:
    :return:
    """
    return ", ".join(df[artist_name].sort_values(ascending=False).index[1:top+1])


print(recommend('Eminem'))
