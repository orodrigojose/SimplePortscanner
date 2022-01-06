# Simple PortScanner

I made a Port scanner Simple for studys

# How to use
### 1. Set permissions on file to used correctly with command:

```
chmod +x scanner.py
```

### 2. Use this command to see scan modes
```
./scanner.py --help
```
> **Output**:
```
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
    
```
### 3. Methods to use cli command in terminal:

Obs.: No't need inform a ports
```
python3 scanner.py -d -p [port here] [IP here]
```

or

- need a the permission mentioned at the beginning
```
./scanner.py -d -p [port here] [IP here]
```

or

- neeed a the permission mentioned at the beginning
```
scanner.py -d -p [port here] [IP here]
```
# Technologies
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
