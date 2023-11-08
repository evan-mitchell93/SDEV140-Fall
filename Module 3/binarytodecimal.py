bString = input("Enter a binary number: ")
exponent = len(bString) - 1
##########
dec = 0
for digit in bString:
    dec += int(digit) * 2 ** exponent
    exponent -= 1

print(f"{bString} to dec: {dec}")