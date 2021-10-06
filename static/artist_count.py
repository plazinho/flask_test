def artist_count():
    """
    Функция для вывода количества исполнителей, находящихся в локальной базе
    :return: число исполнителей
    """
    with open("api/data/artist_names.txt", 'r', encoding="utf-8") as file:
        return len(file.read().strip().split('\n'))
