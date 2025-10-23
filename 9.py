#Count number of lines in a text file

import os

def count_lines(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return len(f.readlines())
    else:
        return "File not found!"

print("Number of lines:", count_lines("sample.txt"))
