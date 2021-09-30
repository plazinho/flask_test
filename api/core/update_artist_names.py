def update_artist_names(name):
    """
    Функция обновляет файл с именами исполнителей, хранящихся в локальной базе
    :param name: Имя исполнителя, которое добавилось в локальную базу
    :return:
    """
    with open("api/data/artist_names.txt", "a") as f:
        f.write(f"{name}\n")
