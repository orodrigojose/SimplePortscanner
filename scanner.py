#!/usr/bin/python3
import sys, time
from socket import *


arguments = sys.argv
arguments.pop(0)

class Scan:
    """
                Guide
                             ┌── Requires ports or values to use mode/command
                             |
    : python3 main.py -f -p 80,81,23 <ip>
                       |  |
                       |  └ Command required to inform ports
                       |
                       └─ Command/Mode to scan

    - Enter ip in the last argument!

              Command information

    -p: to define the ports to be used
    -d: Default scan with 5 seconds timeout [ default ]
    -s: Simple verification using a port scope. EX: 10 to 80 [ simple ]
    -f: Fast scan with an interval of 0.1 seconds, but not very accurate [ fast ]
    
    """
    def __init__(self, IP, ports=[80, 81, 23, 22, 44444, 8080, 6666, 5555], rangePort=[23, 6635]):
        self.ip = IP
        self.ports = ports
        self.openPorts = list()
        self.rangePort = rangePort
        self.connection = socket(AF_INET, SOCK_STREAM)


    def default(self):
        startTime = time.time()

        for port in self.ports:
            self.connection.settimeout(3)
            code = self.connection.connect_ex((self.ip, port))

            if code == 0:
                self.openPorts.append(port)

        time.sleep(1)
        self.connection.close()
        endTime = time.time()
        timeExec = endTime - startTime

        return self.openPorts, timeExec


    def simple(self):
        startTime = time.time()

        for port in range(self.rangePort[0], self.rangePort[1]):
            self.connection.settimeout(1)
            code = self.connection.connect_ex((self.ip, port))
            if code == 0:
                self.openPorts.append(port)

        time.sleep(1)
        self.connection.close()
        endTime = time.time()
        timeExec = endTime - startTime

        return self.openPorts, timeExec


    def fast(self):
        startTime = time.time()

        for port in self.ports:
            self.connection.settimeout(0.3)
            code = self.connection.connect_ex((self.ip, port))
            if code == 0:
                self.openPorts.append(port)

        time.sleep(1)
        self.connection.close()
        endTime = time.time()
        timeExec = endTime - startTime

        return self.openPorts, timeExec


if arguments[0] == '--help':
    print(Scan.__doc__)
    quit()

if '-p' in arguments:
    ports = arguments[arguments.index('-p')+1].split(',')
    portsNum = list()
    try:
        for port in ports:
            portsNum.append(int(port))
    except (ValueError):
        print('Error passing the desired ports')
        quit()
    scanBase = Scan(IP=arguments[-1], ports=portsNum, rangePort=[portsNum[0], portsNum[1]])
else:
    scanBase = Scan(IP=arguments[-1])

modes = {'-f': scanBase.fast, '-s': scanBase.simple, '-d': scanBase.default}
results = modes[arguments[0]]()

if len(results[0]) == 0:
    print("I can't find open ports! Sorry!")
else:
    print('-'*25, f'\n {"PORT":<16}  Status')
    print('-'*25)

    for port in results[0]:
        print(f' {port:.<16}  Open')
    print('-'*25)
    print(f'Time scanning: {results[1]:.<16}  OpenPorts: {len(results[0])}')
