import configparser

co = configparser.ConfigParser()

co['Server'] = {'host': "37.228.138.115",
                'port0': '80',
                'port1': '23',
                'port2': '8080'}

co['delay'] = {'t1': '5'}

with open('info.ini', 'w') as configfile:
    co.write(configfile)
