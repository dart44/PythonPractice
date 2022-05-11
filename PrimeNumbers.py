import math

# isPrime Iterative Function
def isPrime(input_value):
    if input_value > 1:
        sqrt = int(math.sqrt(input_value))
        for i in range(2, sqrt):
            if (input_value % i) == 0:
                print(input_value, "is not a prime number")
                print(i, "times", input_value//i, "is", input_value)
                break
        else:
            print(input_value, "is a prime number")
    else:
        print(input_value, "is not a prime number")

# Input Validation
while True:
    try:   
        n = int(input ('Enter number: '))
    except ValueError:
        print('Please input an integer.')
        continue
    else:
        break

# Output
isPrime(n)