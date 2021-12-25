import pyfiglet
import sys
import socket
from datetime import datetime
banner = pyfiglet.figlet_format("KTU SEC PORT SCANNER")
print(banner)
# argv arguments  python3 main.py 192.123.123.123

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Lutfen ip adresini giriniz !")

date = datetime.now()
string_date = date.strftime("%Y/%m/%d, %H:%M:%S")
print("_"*50)
print(f'Scanning Target : {target}')
print(f'Scanning started at : {string_date}')
print("_"*50)


try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f'Port {port} is open.')
        s.close()
except KeyboardInterrupt:
    print("Kullanıcı tarafından kesildi")
    sys.exit()
except socket.gaierror:
    print("Socket Error ")
    sys.exit()