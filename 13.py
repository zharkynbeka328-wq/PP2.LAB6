#Delete file by specified path (after checks)

import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"{path} deleted successfully.")
        else:
            print("No write permission for this file.")
    else:
        print("File does not exist.")

# Example
delete_file("delete_me.txt")
