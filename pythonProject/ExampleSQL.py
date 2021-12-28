#-------------------------------------------------
"""
"""


"""
    import sqlite3  -   для использования SQLite3
    
    with sqlite3.coonect("имябазы.db") as db:                        -  подключаемся к бд. Если ее нет, то будет создана
        cursor = db.cursor()                                            в то же папке что и программа

    cursor.execute('3 кавычки'CREATE TABLE IF NOT EXISTS employees(  -  создается таблица employees с четырьмя полями
    id integer PRIMARY KEY,                                             id,name,dept,salary, определяется тип полей,     
    name text NOT NULL,                                                 ключевое поле. Тройные кавычки обеспечивают пере
    dept text NOT NULL,                                                 нос кода по строкам
    salary integer);'3 кавычки')

    cursor.execute('''INSERT INTO employees(id,name,dept,salary)     -  вставляем в таблицу employees данные.
        VALUES("1", "Bob", "Sales", "25000")''')                        db.commit - сохраняет изменения
    db.commit()                                                         db.close - последняя строка для закрытия БД    
    db.close()

    так же можно запросить у пользователя данные через input и добавить их в таблицу изменяя предидущую запись так:
        VALUES(?, ?, ?, ?)''',(пользовательские данные)
    
    cursor.execute("SELECT * FROM employees")                        -  выводит все данные * из таблицы
    print(cursor.fetchall())
        for x in cursor.fetchall():                                  -  каждую запись в отдельной строке
            print(x)
    
    FROM employees ORDER BY "name"                                   -  сортирует записи по выбранному полю
    FROM employees WHERE salary > 20000                              -  все записи у которых salary больше 20000
    SELECT бд.поле .... FROM ... AND ...                             -  выбор с условием после AND
    
    cursor.execute("SELECT * FROM бд WHERE поле=?",[пользовательское поле]  выводятся все записи выбранного пользоват. поля
    
    '''SELECT бд.поле ... FROM бд, бд WHERE бд1.поле=бд2.поле'''     -  используется связывание данных через поле
    
    UPDATE бд SET поле = "данные" WHERE условие                      -  обновление данных поля попадающим под условием           
    DELETE FROM бд WHERE условие                                          -  удаление данных согласно условию
"""

"""
    Задание 139 - создание БД Телефонных номеров с полями id, FirstName, Surname, PhoneNumber
"""


import sqlite3

with sqlite3.connect("PhoneBook.db") as db:                                         # подключаемся(создаем) БД
    cursor = db.cursor()
                                                                                    # создаем таблицу Phonebook с полями
cursor.execute(""" CREATE TABLE IF NOT EXISTS PhoneBook(                                 
    id integer PRIMARY KEY,
    FirstName text,
    Surname text,
    PhoneNumber integer); """)
                                                                                    # добавляем данные в таблицу
cursor.execute(""" INSERT INTO PhoneBook(id, FirstName, Surname, PhoneNumber)
VALUES("1", "Simon", "Howels", "01223 39752")""")
db.commit()

cursor.execute(""" INSERT INTO PhoneBook(id, FirstName, Surname, PhoneNumber)
VALUES("2", "Karen", "Phillips", "01954 295773")""")
db.commit()

cursor.execute(""" INSERT INTO PhoneBook(id, FirstName, Surname, PhoneNumber)
VALUES("3", "Darren", "Smith", "01583 749012")""")
db.commit()

cursor.execute(""" INSERT INTO PhoneBook(id, FirstName, Surname, PhoneNumber)
VALUES("4", "Anne", "Jones", "01323 567322")""")
db.commit()

cursor.execute(""" INSERT INTO PhoneBook(id, FirstName, Surname, PhoneNumber)
VALUES("5", "Mark", "Smith", "01223 855534")""")
db.commit()

db.close()

# cursor.execute("SELECT * FROM PhoneBook")
# for x in cursor.fetchall():
#    print(x)
