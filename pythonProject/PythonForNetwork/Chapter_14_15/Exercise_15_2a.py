#-------------------------------------------------
"""
"""

"""
    Задание 15.2a
    Создать функцию convert_to_dict, которая ожидает два аргумента:
        * список с названиями полей
        * список кортежей со значениями
    Функция возвращает результат в виде списка словарей,
    где ключи - взяты из первого списка, а значения подставлены из второго.
    Проверить работу функции:
        * первый аргумент - список headers
        * второй аргумент - список data
"""

from pprint import pprint

headers = ["hostname", "ios", "platform"]

data = [
    ("R1", "12.4(24)T1", "Cisco 3825"),
    ("R2", "15.2(2)T1", "Cisco 2911"),
    ("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L"),
]

result = []

def convert_to_dict(headers, sh_list):
    """
    через генератор словаря return [dict(zip(headers, i)) for i in sh_list]
    :param headers: список с названиями полей
    :param sh_list: список кортежей со значениями
    :return: список словарей вида [{headers:data}]
    """
    for i in sh_list:
        result.append(dict(zip(headers, i )))
    return result

if __name__ == "__main__":
    pprint(convert_to_dict(headers, data))