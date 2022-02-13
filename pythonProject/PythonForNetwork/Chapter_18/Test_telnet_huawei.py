import telnetlib
import time
from pprint import pprint


def to_bytes(line):
    return f"{line}\n".encode("utf-8")


def send_show_command(ip, password, commands):
    with telnetlib.Telnet(ip) as telnet:
        telnet.read_until(b"Password:")
        telnet.write(to_bytes(password))
        time.sleep(3)
        telnet.read_very_eager()

        result = {}
        for command in commands:
            telnet.write(to_bytes(command))
            output = telnet.read_until(b">", timeout=5).decode("utf-8")
            result[command] = output.replace("\r\n", "\n")
        return result


if __name__ == "__main__":
    devices = ["192.168.75.133", "192.168.75.134", "192.168.75.135"]
    commands = ["disp ip int br", "disp int desc"]
    for ip in devices:
        result = send_show_command(ip, "huawei", commands)
        print(f"Huawei {ip}: ")
        pprint(result, width=180)