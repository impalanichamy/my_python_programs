                            
#!/usr/bin/env python

import subprocess

interface = input("Enter the interface name :")

new_mac = input("Enter the new mac address :")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])


print("[+] successfully changed " + interface + "mac address to" + new_mac )







