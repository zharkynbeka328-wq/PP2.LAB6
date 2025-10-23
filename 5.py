#Check if all elements of a tuple are true

def all_true(t):
    return all(t)

# Example
print(all_true((True, True, False)))  # False
print(all_true((1, 2, 3)))            # True
