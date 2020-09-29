#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="interface for choose eth0 or w>
parser.add_option("-m", "--mac", dest="new_mac", help="enter the new mac")

(options, arguements)=  parser.parse_args()
interface =  options.interface

new_mac =  options.new_mac

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])


print("[+] successfully changed " + interface + "mac address to" + new_mac )




