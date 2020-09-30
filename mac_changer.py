  GNU nano 5.2                                                                                                    mac_changer.py                                                                                                              
#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="enter the interface to change mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="enter the new mac address")
    (options, arguements) = parser.parse_args()
    if not options.interface:
        parser.error("[-] make sure you have enter interface name . for more info see in --help")
    elif not options.new_mac:
        parser.error("[-] make sure you have enter new mac addess. for more info see in --help")
    return options


def change_mac(interface, new_mac):
    print("[+] successfully changed mac address for " + interface )     
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    

options = get_arguments()
change_mac(options.interface,  options.new_mac)



