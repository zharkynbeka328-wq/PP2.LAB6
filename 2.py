#Count uppercase and lowercase letters in a string

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("No. of Upper case characters:", upper)
    print("No. of Lower case characters:", lower)

# Example
count_case("Hello World!")
