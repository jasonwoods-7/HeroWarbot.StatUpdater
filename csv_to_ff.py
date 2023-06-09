#!/usr/local/bin/python3

import csv
import pyperclip

with open('hero_stats.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')

    powers = []
    for row in reader:
        powers.append(' '.join(row))

    pyperclip.copy(' '.join(powers))
