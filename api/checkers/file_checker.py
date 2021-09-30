import os
import json


def file_checker(file_path):
    """
    Функция проверяет наличие словаря, состоящего из исполнителей(ключи) и всех их обработанных текстов песен(значения)
    Если этого файла нет, то производится запуск скрипта init_script.py для создания первоначальной локальной базы
    :param file_path: путь до файла dictionary_words.json
    :return:
    """
    if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
        # checks if file exists
        print("File exists and is readable")
    else:
        print("Either file is missing or is not readable, creating file and starting init_script.py...")
        with open(f'{file_path}', 'w', encoding="utf-8") as f:
            f.write(json.dumps({}))
        data_path = 'api/data/raw_data'
        if not os.path.exists(data_path):
            os.mkdir(data_path)
        import api.core.init_script
