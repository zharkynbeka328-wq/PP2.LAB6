#Write a list to a file

def write_list_to_file(filename, data_list):
    with open(filename, 'w') as f:
        for item in data_list:
            f.write(f"{item}\n")

# Example
write_list_to_file("output.txt", ["Apple", "Banana", "Cherry"])
