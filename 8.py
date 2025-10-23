#Test whether path exists; find filename and directory

import os

path = "example_folder/example.txt"

if os.path.exists(path):
    print("File exists.")
    print("Filename:", os.path.basename(path))
    print("Directory:", os.path.dirname(path))
else:
    print("Path does not exist.")
