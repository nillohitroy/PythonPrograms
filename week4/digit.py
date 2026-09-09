digit = input("Enter a number: ")

if not digit.isdigit():
    print("It is not a digit")
    
else:
    next_digit = ""
    for char in digit:
        shift = (int(char) + 1) % 10
        next_digit += str(shift)
        
print("Shifted digits: ", next_digit)
        
print("Next Number: ", int(digit) + 1)