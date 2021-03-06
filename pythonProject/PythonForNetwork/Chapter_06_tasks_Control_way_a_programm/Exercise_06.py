#-------------------------------------------------
"""
"""


"""
    При использовании со словарями условие in выполняет проверку по КЛЮЧАМ словаря.
    
    В Python оператор AND возврщает значение одного из операндов. Если оба операнда является истиной, 
    результатом выражения будет последнее значение. Если оба операнда является ложью, результатом будет первое 
    ложное значение.
    
    Оператор OR как и AND возвращает значение одного из операндов - первый истинный. Если все значения ложные 
    - возвращается последнее значение. Операнды после ИСТИНЫ не вычисляются.
    
    Для вывода пары ключ-значение в цикле:
    for key in r1:
        print(key + " => " + r1[key]    
    или
    for key,value in r1.items()
        print(key + " => " + value
    
    break - досрочное прерывание цикла; continue - возвращает управление в начало цикла
    
    Для работы с икслючениями используется try / except / finally(выполянется всегда). raise <ИМЯ> - генерирует исключение
"""

"""
    Задание 6.1 - Преобразовать mac адреса к нужному формату и добавить их в список result. Список вывести.
    Формат MAC - xxxx.xxxx.xxxx
"""

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []

for i in mac:
    result.append(i.replace(':','.'))

print("Список MAC: ",result)

