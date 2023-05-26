#!/usr/local/bin/python3

import pyperclip

command = ""

with open('hero_stats.csv', 'r', encoding='utf-8') as f:
    for line in f:
        split = line.rstrip('\n').split(',')
        command += split[0] + " " + split[1] + " "

pyperclip.copy(command)
