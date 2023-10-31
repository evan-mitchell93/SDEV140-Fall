primaryColors = ['yellow','blue','red']
secondaryColors = ['purple','orange','green']

primaryOne = (str(input("Enter color:")))
primaryTwo = (str(input("Enter a color again:")))

if primaryOne and primaryTwo in primaryColors:
    print("Yes")
    if primaryOne == ("red" or "yellow"):
        print("orange")
else:
    print("No")