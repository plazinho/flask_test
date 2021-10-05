def artist_checker(name: str) -> str:
    """
    Функция проверяет наличие исполнителя в локальной базе.

    :param name: Имя исполнителя
    :return:
    """
    with open("api/data/artist_names.txt", "r", encoding="utf-8") as file:
        names = file.read().strip().split('\n')
        if name in names:
            return name
        return 'not in DB'
