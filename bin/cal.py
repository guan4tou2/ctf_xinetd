#!/usr/bin/python3
with open('/home/ctf/flag', 'r') as f:
    for _ in f.read():
        print(ord(_))
