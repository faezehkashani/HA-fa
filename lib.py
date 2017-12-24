import os


def check_ip():

    hostname = "192.168.56.1"
    response = os.system("ping -c 4 "+hostname)
    if response == 0:
        return hostname, "is up"
    else:
        return hostname, "is down"
