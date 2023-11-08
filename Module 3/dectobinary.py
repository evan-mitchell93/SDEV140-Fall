dec = int(input("Enter a decimal number: "))
if dec == 0:
    print(0)
else:
    binary = ""
    while dec > 0:
        remainder = dec % 2
        binary = str(remainder) + binary
        dec = dec // 2
    print(binary)