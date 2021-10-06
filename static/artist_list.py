def artist_list():
    """
    Функция для вывода отсортированного списка исполнителей, находищихся в локальной базе
    :return: список исполнителей
    """
    with open("api/data/artist_names.txt", 'r', encoding="utf-8") as file:
        return '\n'.join(sorted(file.read().strip().split('\n'))).replace('_', '/')
