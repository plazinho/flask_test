import os
import json


def files_checker(json_path="api/data/dictionary_words.json",
                  raw_data_path="api/data/raw_data",
                  init_path="api/data/init_names.txt"):
    """
    Функция проверяет наличие словаря, состоящего из исполнителей(ключи) и всех их обработанных текстов песен(значения)
    Если этого файла нет, то производится запуск скрипта init_script.py для создания первоначальной локальной базы
    :param raw_data_path: путь до папки, куда будут записываться файлы с текстами песен исполнителей
    :param init_path: путь до файла с именами исполнителей для создания первоначальной базы
    :param json_path: путь до словаря с исполнителями и их обработанными текстами песен - на основе этого файла будет
    рассчитываться матрица косинусной близости текстов песен исполнителей
    :return: результат проверки
    """
    # проверка существования папки, куда будут записываться файлы с текстами песен исполнителей
    if not os.path.exists(raw_data_path):
        os.mkdir(raw_data_path)
        print("Directory for lyrics 'api/data/raw_data' does not exist, creating...")
    else:
        print("Directory for lyrics 'api/data/raw_data' exists - check")

    # проверка существования словаря с исполнителями и их обработанными текстами песен
    if os.path.isfile(json_path) and os.access(json_path, os.R_OK):
        print("File 'api/data/dictionary_words.json' exists and is readable - check")
        return 'OK'
    else:
        # создаем пустой словарь, если его не существует
        print("Either file 'api/data/dictionary_words.json' is missing or is not readable, creating...")
        with open(f'{json_path}', 'w', encoding="utf-8") as f:
            f.write(json.dumps({}))
        # проверка существования файла с именами исполнителей для создания первоначальной базы
        if os.path.isfile(init_path) and os.access(init_path, os.R_OK):
            print("File api/data/init_names.txt exists and is readable - check")
            return 'initializing'
        else:
            print("Either file 'api/data/init_names.txt' is missing or is not readable")
            return 'init file does not exist'
