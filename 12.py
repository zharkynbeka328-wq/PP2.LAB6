#Copy contents of one file to another

import os

def copy_file(src, dest):
    if os.path.exists(src):
        with open(src, 'r') as f1, open(dest, 'w') as f2:
            f2.write(f1.read())
        print(f"Copied from {src} to {dest}")
    else:
        print(f"Source file '{src}' not found!")

copy_file("source.txt", "copy.txt")
