import lib
import time
import configparser
import signal
import sys


def signal_handler(signal, frame):             # Exit function (by press Ctrl+C)
    print('You pressed Ctrl+C!')
    sys.exit(0)

result = 1                                     # Result of communicating with the server
server_info = open("Result.txt", 'w')          # Opening file to store server information

conf_main = configparser.ConfigParser()        # Read config file
conf_main.read('info.ini')

hostname = conf_main['Server']['host']
delay_time = int(conf_main['delay']['t1'])     # Setting the check time

while True:
    server_info.write('ping: ')

    while result == 1:                         # Checking Ping hostname
        result = lib.ping_ip(hostname)
        server_info.write(str(result))
        time.sleep(delay_time)

    result = 1
    server_info.write('\n\ntelnet: \n')

    for i in range(3):
        port = conf_main['Server']['port%d' % i]
        server_info.write('port = %s : ' % port)
        while result == 1:                     # Checking telnet hostname
            result = lib.telnet_port(hostname, port)
            server_info.write(str(result))
            time.sleep(delay_time)
            signal.signal(signal.SIGINT, signal_handler)
