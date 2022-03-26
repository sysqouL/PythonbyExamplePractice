#!D:\PythonByExampleExercise\venv\Scripts\python.exe
#-------------------------------------------------
"""
"""

"""
    Задание 7.2 - создать срипт обрабатывающий файл config_sw1.txt. Имя файла передается как аргумент. 
    В выводе исключаются строки которые начинаются с !.
    Задание 7.2a - не должны выводится команды, в которых содержатся игнорируемые слова
    Задание 7.2b - записать в файл результат
"""

# from sys import argv

# file = argv[1]
# file_res = argv[2]
ignore = ["duplex", "alias", "configuration"]

with open("config_sw1.txt") as f:
    with open("config_sw1_ignore.txt", "w") as i:                       # with open(file) as f, open(file_res) as i:
        for line in f:
            line = line.rstrip()
            if "!"  not in line:                                        # if not line.startswith("!")
                if ignore[0] not in line:
                    if ignore[1] not in line:
                        if ignore[2] not in line:
                            i.write(line+"\n")
"""
    можно с помощью множеств: delete = set(line).intersection(set(ignore)) или & тогда if примет вид:
    if not line.startswith("!") and not delete:
"""