#List only directories, files, and all in a path

import os

path = "."

print("Directories:")
print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

print("\nFiles:")
print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

print("\nAll (directories and files):")
print(os.listdir(path))
