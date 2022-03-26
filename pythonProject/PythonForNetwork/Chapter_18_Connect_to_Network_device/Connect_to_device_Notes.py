#-------------------------------------------------
"""
"""

"""
            Модули:
                - pexpect (реализация expect на Python): работа с любой интерактивной сессией 
                (ssh, telnet, sftp и т.п.), позволяет выполнять различные команды в ОС
                - telnetlib - позволяет подключаться по Telnet
                - paramiko - подключение по SSHv2
                - netmiko - обёртка paramiko, для работы с сетевым оборудованием
                - scapli - подключение по SSHv2, Telnet, NETCONF
                
            Для скрытия пароля при вводе в момент подключения можн использовать модулю getpass:
                import getpass
                password = getpass.getpass()
            Еще один вариант хранения пароля(имени) - переменные окружения:
                $ export SSH_USER=user
                $ export SSH_PASSWORD=userpass
                
                import os
                USERNAME = os.environ.get('SSH_USER')
                PASSWORD = os.environ.get('SSH_PASSWORD')             
"""

#---------------------------------------------------------------------------------------------------------------

"""
            Модуль pexpect
            Подключения: Telnet, SSH, ftp
            Установка: pip install pexpect
            Логика работы:
                - запускается прграмма
                - pexpect ожидает вывод(приглашение, пароль и т.п.)
                - получив вывод, отправляет команды/данные
                - последние два действие повторяются N-количество раз
            
            pexpect.spawn - позволяет взаимодействовать с программой, отправляя данные и ожидая ответ
            Инициация SSH соединения:
                ssh = pexpect.spawn('ssh cisco@192.168.100')
                ssh.expect('[Pp]assword') - ожидание пароля
                ssh.sendline('cisco') - отправка пароля
                
            Пример - в режим enable и отправка команды:
                ssh.expect('[>#]')
                ssh.sendline('enable')
                ssh.expect('[Pp]assword')
                ssh.sendline('cisco')
                ssh.expect('[>#]')
                ssh.sendline('sh ip int br')
                ssh.expect('#')
                Вывод команды находится в атрибуте before в виде последовательности байтов
                show_output = ssh.before.decode('utf-8')
                print(show_output)
            Завершение сессии:
                ssh.close()
                
            Pexpect не интерпретирует спец символы: >, |, *
            Пример с командой ls -ls | grep SUMMARY:
                import pexpect
                p = pexpect.spawn('/bin/bash -c "ls -ls | grep pexpect"')
                p.expect(pexpect.EOF) - вывод будет 0, EOF - признак конца файла
                print(p.before.decode('utf-8'))
                EOF - спец значение которое позволяет отреагировать на завершение исполнения команды или сессии в spawn
                
            В pexpect.expect как шаблон может использоваться:
                - регулярное выражение
                - EOF
                - TIMEOUT - исключение timeout (30 сек по умолчанию)
                - compiled re
            Передача списка значений:
                p = pexpect.spawn('/bin/bash -c "ls -ls | grep netmiko"')
                p.expect(['py3_convert', pexpect.TIMEOUT, pexpect.EOF]) 
"""

#---------------------------------------------------------------------------------------------------------------

"""
            Модуль Telnetlib
            Подключение:
                telnet = telnetlib.Telnet('ip')
            Telnetlib требует передачу байтовой строки а не обычной
            
            read_until - указывается до какой строки считать вывод. Возвращает все до указанной строки
                telnet.read_until(b'Username')
            
            write - для передачи данных
            Читаем вывод до слова Password и передаем пароль, отправялем команду
                telnet.read_until(b'Password')
                telnet.write(b'cisco\n')
                telnet.read_until(b'>')
                telnet.write(b'sh int brf\n')
            
            read_very_eager - можно отправить несколько команд, а затем считать вывод
                telnet.write(b'sh arp\n')
                telnet.write(b'sh clock\n')
                telnet.write(b'sh ip int br\n')
                all_result = telnet.read_very_eager().decode('utf-8')
                print(all_result)
            ПЕРЕД МЕТОДОМ VERY_EAGER ВСЕГДА НАДО СТАВИТЬ time.sleep(n)
            Через red_until:
                telnet.write(b'sh arp\n')
                telnet.write(b'sh clock\n')
                telnet.write(b'sh ip int br\n')    
                telnet.read_until(b'>')
                    вывод sh arp
                telnet.read_until(b'>')
                    вывод sh clock
                telnet.read_until(b'>')
                    вывод sh ip int br
                    
            Реакция на отсутствие вывода:
                read_until ждёт строку, если ее нет - метод зависает. Опцианально указывает параметр timeout
                telnet.read_until(b'>', timeout=5)
            Если за указанное время строка не появилась, возвращается пустая строка - b''
            Метод read_very_eager() вернет пустую строку - b''
            
            Метод expect позволяет указывать список с регулярными выражениями. В telnetlib всегда надо передавать
            список регулярных выражений.
                telnet.write(b'sh clock\n')
                telnet.expect([b'[>#]'])
                Возвращает:
                    - индекс выражения, которое совпало
                    - объект Match
                    - байтовая строка, которая содержит все считанное до регулярного выражения и включая его
            
            закрытие сессии - telnet.close()
"""

#---------------------------------------------------------------------------------------------------------------

"""
            Модуль paramiko
            Установка: pip install paramiko
            
            Подключение:
                - сначала создается клиент и выполняется его настройка, затем выполняется подключение и получение
                интерактивной сессии
                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  - указывает политику(необезательно)
                    client.connect(hostname='ip',username='username',password='pas',
                    look_for_keys=False, allow_agent=False)
                    ssh = client.invoke_shell()
                    
                    AutoAddPolicy() - автоматически добавляет новое имя хоста и ключ в локальный объект HostKeys
                    метод connect выполняет подключение к SSH-серверу и аутентифицир подключение
                        look_for_keys - отключает аутентификац по ключам 
                        allow_agent - отключение подключения к локальному агенту ОС
                    
                    invoke_shell() - устанавливает интерактивную сессию SSH с сервером
                    
            Метод send - отправляет указанную строку в сессию и возвращает количество отправл байт или ноль
            если сессия закрыта
                ssh.send("enable\n") - вернет 7
                
            Метод recv - получает данные из сессии. В скобках указывается max значение в байтах которое нужно получить
                ssh.recv(3000) - вернет строку
                
            Метод close - закрывает сессию:
                ssh.close() 
"""