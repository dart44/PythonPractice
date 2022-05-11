def isArmstrongNumber(number):
    number = str(number)
    digits = list(number)
    sum = 0

    for digit in digits: 
        sum += pow(int(digit), 3)

    if (int(number) == sum):
        print(number + ' is an Armstrong Number.')
        return True
    else:
        print (number + ' is not an Armstrong Number.')
        return False

# Test
def test_numbers():
    assert isArmstrongNumber(153)
    assert not isArmstrongNumber(135)

# User Input & Validation
while True:
    try:   
        n = int(input ('Enter number: '))
    except ValueError:
        print('Please input an integer.')
        continue
    else:
        break

# Function Call
isArmstrongNumber(n)