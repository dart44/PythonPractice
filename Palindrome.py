# Function Definitions - Reverse string using a for loop
def reverse_string(str):
    reverse = ""
    for i in str:
        reverse = i + reverse
    return reverse

# Determine if a string is a palindrome
def isPalindrome(input_value):
    if input_value == reverse_string(input_value):
        return True
    else:  
        return False

# PyTests
def test_true():
    assert isPalindrome('noon')
def test_false():
    assert not isPalindrome('robot')

# Test script
def main():
    # User Input & Validation
    while True:
        try:   
            s = str(input ('Enter text: '))
        except ValueError:
            print('Please input a string.')
            continue
        else:
            break
    
    # Function Call
    if isPalindrome(s) is True:
        print(f'{s} is a palindrome')
    else:
        print(f'{s} is not a palindrome')

# Run test script if this file is not being imported
if __name__ == '__main__':
    main()
