import os
from telnetlib import Telnet


def ping_ip(hostname):

    response = os.system("ping -c 4 " + hostname)
    if response == 0:  # if server is uptime then response=0
        return 1
    else:
        return 0


def telnet_port(hostname, port):
    try:
        tn = Telnet()
        tn.open(hostname, port)
        tn.close()
        return 1

    except IOError:
        return 0


#  rep = os.system("telnet " +hostname +" " +port1)
