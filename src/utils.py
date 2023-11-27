import json


def load_operation(path: str) -> list[dict]:
    """
    Чтение операций из файла
    :param path: путь к файлу
    :return: json c операциями
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)
