# Recursive Function Definition and Memoization
from functools import lru_cache
@lru_cache(maxsize = 1000)
def factorial(input_value):
    if input_value < 2: 
        return 1
    elif input_value >= 2:
        return input_value * factorial(input_value-1)

# Input Validation
while True:
    try:   
        n = int(input ('Enter upper bound (inclusive): '))
    except ValueError:
        print('Please input an integer.')
        continue
    else:
        break

# Output
for i in range(1, n+1):
     print(f"{i}! = ", factorial(i))