#!/usr/local/bin/python3

import csv
import pyperclip

command = ""

with open('hero_stats.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        command += ' '.join(row) + ' '

pyperclip.copy(command.rstrip(' '))
