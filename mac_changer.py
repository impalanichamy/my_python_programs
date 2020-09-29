                                
#!/usr/bin/env python

import subprocess

interface = input("Enter the interface name :")

new_mac = input("Enter the new mac address :")

subprocess.call(" ifconfig "  + interface + " down " , shell=True)
subprocess.call(" ifconfig " + interface + " hw ether " + new_mac , shell=True)
subprocess.call(" ifconfig " + interface + " up " , shell=True)


print("[+] successfully changed " + interface + "mac address to" + new_mac )


