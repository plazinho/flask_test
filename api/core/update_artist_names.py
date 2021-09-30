def update_artist_names(name):
    """
    Функция обновляет файл с именами исполнителей, хранящихся в локальной базе
    :param name: Имя исполнителя, которое добавилось в локальную базу
    :return:
    """
    with open("api/data/artist_names.txt", "a", encoding="utf-8") as f:
        f.write(f"{name}\n")
