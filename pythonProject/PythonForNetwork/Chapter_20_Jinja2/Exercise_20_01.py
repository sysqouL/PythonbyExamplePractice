#-------------------------------------------------
"""
"""

"""
    Задание 20.1
    Создать функцию generate_config.
    Параметры функции:
    * template - путь к файлу с шаблоном (например, "templates/for.txt")
    * data_dict - словарь со значениями, которые надо подставить в шаблон
    Функция должна возвращать строку с конфигурацией, которая была сгенерирована.
"""

import yaml
import os
from jinja2 import Environment, FileSystemLoader


def generate_config(template, data_dict):
    """
    :param template: путь к файлу с шаблоном
    :param data_dict:  словарь со значениями для подстановки в шаблон
    :return: templ.render(data_dict) - подставляет значения из data_dict в шаблон templ
    """
    template_dir, template_file = os.path.split(template)
    env = Environment(
        loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True
    )
    templ = env.get_template(template_file)
    return templ.render(data_dict)


if __name__ == "__main__":
    data_file = "data_files/for.yaml"
    template_file = "templates/for.txt"
    #data_file = "data_files/router_info.yaml"
    #template_file = "templates/cisco_router_base.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))