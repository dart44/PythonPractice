# Recursive Function Definition and Memoization
from functools import lru_cache
@lru_cache(maxsize = 1000)
def fibonacci(input_value):
    if input_value == 0: 
        return 0
    elif input_value == 1 or input_value == 2:
        return 1
    else:
        return fibonacci(input_value-1) + fibonacci(input_value-2)

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
     print(f"F{i} = ", fibonacci(i))