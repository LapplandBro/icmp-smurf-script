# IP Spoofing - Smurf Attack

> ICMP Echo attack  - flood the target with ping traffic

## Usage

```
$ python main.py -h
usage: main.py [-h] -s SourceIP -d DestinationIP -n Count [-l Size]

Ip Spoofing - Smurf Attack

optional arguments:
  -h, --help                             show this help message and exit
  -s SourceIP, --src SourceIP            Enter IP to spoof
  -d DestinationIP, --dst DestinationIP  Enter IP that will send the echo
                                         replay
  -n Count, --count Count                amount of packets to send
  -l Size, --size Size                   Set buffer size
```

Example:

```
$ python main.py -s 10.10.10.10 -d 192.168.43.1 -n 50 -l 100 
```

## Requirements

- [scapy](https://pypi.org/project/scapy/)
- [argparse](https://pypi.org/project/argparse/)

Example using pip:

```
pip install -r requirements.txt
```

Tested with python 3.7.

## NOTICE
All the content uploaded to this repository is for learning propose only. Using the content is on your own responsibility.
