#input of 2 numbers
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a second number: "))

#check the the bigger number in number1 and number2
if number1 > number2:
    print(f"The number {number1} is bigger than {number2}")
elif number2 > number1:
    print(f"The number {number2} is bigger than {number1}")
else:
    print("Both number is the same")