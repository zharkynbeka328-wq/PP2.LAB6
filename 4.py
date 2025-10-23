#Invoke square root after specific milliseconds

import math
import time

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} miliseconds is {result}")

# Example
delayed_sqrt(25100, 2123)
