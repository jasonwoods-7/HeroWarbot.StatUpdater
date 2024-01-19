#!/usr/local/bin/python3

import csv
import sys

def space_separated_to_csv(data):
    # Create a CSV writer to write to stdout
    csv_writer = csv.writer(sys.stdout, delimiter=',')

    # Write the data to stdout with every two elements on a new line
    for i in range(0, len(data), 2):
        csv_writer.writerow(data[i:i+2])

if __name__ == "__main__":
    # Check if the number of command-line arguments is even
    if len(sys.argv) % 2 != 1:
        print("Usage: python script.py Aidan 0 Alvanor 0 Amira 0")
        sys.exit(1)

    # Read input data from command-line arguments
    input_data = sys.argv[1:]

    space_separated_to_csv(input_data)
