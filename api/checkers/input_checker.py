from static.texts import INPUT_ERROR


def input_checker(name: str) -> str:
    """
    Проверка входных данных от пользователя на случай, если это не текст
    :param name: запрос от пользователя
    :return: исходный запрос, если все в порядке
    """
    if isinstance(name, str):
        return name
    else:
        print(INPUT_ERROR)
