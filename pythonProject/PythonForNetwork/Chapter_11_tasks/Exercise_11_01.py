#-------------------------------------------------
"""
"""

"""
    Задание 11.1
    Создать функцию parse_cdp_neighbors, которая обрабатывает вывод команды show cdp neighbors.
    У функции должен быть один параметр command_output, который ожидает как аргумент
    вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
    файла в строку, а затем передать строку как аргумент функции.
    Функция должна возвращать словарь, который описывает соединения между устройствами.
"""


def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    result = {}
    for line in command_output.split("\n"):
        line = line.strip()
        columns = line.split()
        if ">" in line:
            hostname = line.split(">")[0]
        elif len(columns) > 3 and columns[3].isdigit():
            deviceID, loacl_int, local_int_num, *other, port, ID = columns
            result[(hostname, loacl_int + local_int_num)] = (deviceID, port + ID)
    return result


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))