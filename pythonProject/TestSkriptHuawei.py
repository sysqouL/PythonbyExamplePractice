import telnetlib
import time

host='192.168.75.128'
password='huawei'

tn=telnetlib.Telnet(host)

tn.read_until(b"Password:")
tn.write(password.encode('ascii') + b"\n")
tn.write(b'display cu \n')

time.sleep(1)

result = tn.read_very_eager().decode('ascii')

print(result)
tn.close()

