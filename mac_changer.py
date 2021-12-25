import subprocess
import optparse
import re



# terminalden komut al
# mac adresini değiştirmeye çalış
# teyit etmesi gerekiyor


def get_command():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Degistirmek istediginiz arayüz")
    parser.add_option("-m", "--macAddress", dest="mac_address", help="yeni mac adresi")
    return parser.parse_args()

def change_mac(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])


def control_mac(user_interface):
    ifconfig = subprocess.check_output(["ifconfig", user_interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if new_mac:
        result = new_mac.group(0)
    else:
        result = None
    return result


(user_input, args) = get_command()
change_mac(user_input.interface, user_input.mac_address)
final_mac = control_mac(user_input.interface)
if final_mac == user_input.mac_address:
    print("Başarlı ! ")
else:
    print("Mac Adresiniz değiştirilemedi ... ")


