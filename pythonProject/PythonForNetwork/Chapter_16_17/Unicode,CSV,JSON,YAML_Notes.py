#-------------------------------------------------
"""
"""

"""
    "зашифровать" строку в байты (str -> bytes) - используется метод encode
    "расшифровать" байты в строку (bytes -> str) - используется метод decode
    Пример:
        hi = 'привет'
        hi.encode('utf-8'):
        b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
        hi_bytes = hi.encode('utf-8')
        
        hi_bytes.decode('utf-8'): 'привет'
        
        str.encode(hi, encoding='utf-8')
        bytes.decode(hi_bytes, encoding='utf-8'
        
    При работе с файлами лучше явно указывать кодировку, так как в разных ОС она может отличаться:
        with open('r1.txt', encoding='utf-8') as f:
            for line in f:
            
    ASCII не преобразует в байты кириллицу
    
    CSV: Получение заголовков столбцов отдельным объектом:
        import csv
        
        with open('file.csv') as f:
        reader = csv.reader(f, delimiter =''(разделитель))
        headers = next(reader)
        print('Headers:', headers)
        for row in reader:
            print(row)
    
    Получение словарей: ключи - названия столбцов, значения - значения столбцов:
        import csv
        
        with open('file.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
                print(row['key'], row['value'])
        
    Запись в файл:
        with open('file.csv', 'w') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)
"""

# ------------------------------------------------------------------------------------------------------------

"""
    Для чтения в модуле JSON есть два метода:
        - json.load - метод считывает файл в формате JSON и возвращает объекты Python
        - json.loads - метод считывает стркоу в формате JSON и возвращает объекты Python
    
    Пример json.load:
        import json
        
        with open('file.json') as f:
            templates = json.load(f)
        print(templates)
        
        for section, commands in templates.items():
            print(section)
            print('\n'.join(commands))
        
    Пример json.loads:
        import json
        
        with open('file.json') as f:
            file_content = f.read()
            templates = json.loads(file_content)
        print(templates)
        
        for section, commands in templates.items():
            print(section)
            print('\n'.join(commands))        

    Для записи файла в формате JSON:
        - json.dump() - метод записывает объект Python в файл в формате JSON
        - json.dumps() - метод возвращает строку в формате JSON
    dump лучше подходит для записи ифнормации в формате JSON в файл
    dumps для ситуации когда надо вернуть строку в формате JSON (и ее передаче)
    
        --- Кортежи при записи в JSON превращаются в списки
        --- В формат JSON нельзя записать словарь, у которого ключи - кортежи (можно их игнорировать 
        с помощью доп параметра)
        --- Ключами словаря могут быть только строки (числа конвертируются в строки)
"""

# ------------------------------------------------------------------------------------------------------------

"""
    В YAML нельзя использовать знаки табуляции (используются пробелы)
    Список:
        [switchport mode access, switchport access vlan]
        или:
        - switchport mode acccess
        - switchport access vlan
    
    Словарь:
        { vlan: 100, name: IT}
        или:
        vlan: 100
        name: IT
    
    Комбинации:
    Словарь с двумя ключами
    access:
    - switchport mode acccess
    - switchport access vlan
    trunk:
    - switchport mode trunk
    - switchport trunk allowed vlan    
    
    Список словарей:
    - BS: 1550
      IT: 791
    - BS: 1510
      IT: 793
      
    Чтение из YAML:
    import yaml
    from pprint import pprint
    
    with open('file.yaml') as f:
    templates = yaml.safe_load(f)
    pprint(templates)  
"""