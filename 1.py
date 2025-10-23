#Multiply all numbers in a list

from functools import reduce

def multiply_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

# Example
nums = [2, 3, 4, 5]
print("Result:", multiply_list(nums))
