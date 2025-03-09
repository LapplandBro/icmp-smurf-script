# IP Spoofing - Smurf Attack

> ICMP-эхо-атака - залить цель пинговым трафиком.

## Использование

```
$ python main.py -h
Использование: main.py [-h] -s SourceIP -d DestinationIP -n Count [-l Size]

Ip Spoofing - Smurf Attack

необязательные аргументы:
  -h, --help показать это справочное сообщение и выйти
  -s SourceIP, --src SourceIP Введите IP для подмены
  -d DestinationIP, --dst DestinationIP Введите IP, с которого будет отправлено эхо
                                         воспроизведение
  -n Count, --count Количество пакетов для отправки
  -l Size, --size Размер Установите размер буфера.
```

Пример:

```
$ python main.py -s 10.10.10.10 -d 192.168.43.1 -n 50 -l 100 
```

## Требования

- [scapy](https://pypi.org/project/scapy/)
- [argparse](https://pypi.org/project/argparse/)

Пример с использованием pip:

```
pip install -r requirements.txt
```

Проверено с python 3.7.

## ВНИМАНИЕ
Все материалы, загруженные в этот репозиторий, предназначены только для обучения. Использование содержимого является вашей собственной ответственностью.

Переведено с помощью DeepL.com (бесплатная версия)
